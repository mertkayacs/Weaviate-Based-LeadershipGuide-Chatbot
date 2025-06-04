import os
import weaviate
from datetime import datetime

from langchain_weaviate import WeaviateVectorStore
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_community import GoogleSearchAPIWrapper
from langchain.prompts import PromptTemplate
#For huggingface
os.environ["TOKENIZERS_PARALLELISM"] = "false"
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

#Weaviate Client
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
)


try:
    #LangChain Top3
    vector_store = WeaviateVectorStore(
        client=client,
        index_name="LeadershipContent",
        text_key="chunk",
    )
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    #Question and retrieval
    question = "Vergi yasaları nelerdir?"
    docs = retriever.invoke(question)
    combined_context = "\n".join([doc.page_content for doc in docs])

    #Fallback Rules
    generic_phrases = [
        "bilmiyorum",
        "bilgiye ulaşamadım",
        "kaynak bulunamadı",
        "bu soruya yanıt veremiyorum",
        "bu konuda yeterli bilgi yok",
        "yanıt verememekteyim",
        "üzgünüm"
    ]

    lower_context = combined_context.lower()
    contains_generic_phrase_context = any(phrase in lower_context for phrase in generic_phrases)
    too_short = len(combined_context.strip()) < 100

    def do_google_fallback():
        search = GoogleSearchAPIWrapper(k=3)
        current_year = datetime.now().year
        search_query = f"{question} after:{current_year - 1}"
        web_results = search.run(search_query)

        llm = ChatOpenAI(model="gpt-4o", temperature=0)
        prompt = PromptTemplate(
            template="Soru: {question}\nWeb Sonuçları: {web_results}\nCevabı Türkçe ve profesyonel bir şekilde ver. Son web aramaları günceldir ve yıl {current_year}, buna dikkat et.",
            input_variables=["question", "web_results", "current_year"]
        )
        final_answer = (prompt | llm).invoke({
            "question": question,
            "web_results": web_results,
            "current_year": current_year
        })

        print("\n Google search based answer:")
        print(final_answer.content)
        print("\n Google Kaynakları:")
        print(web_results)

    if contains_generic_phrase_context or too_short:
        print("\nFallback : Context too generic or short")
        do_google_fallback()
    else:
        #Final Answer from Weaviate
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
        prompt = PromptTemplate(
            template="Soru: {question}\nVerilen bilgi: {context}\nCevabı Türkçe ve profesyonel şekilde ver.",
            input_variables=["question", "context"]
        )
        final_answer = (prompt | llm).invoke({
            "question": question,
            "context": combined_context
        })

        final_answer_text = final_answer.content.lower()
        contains_generic_phrase_final = any(phrase in final_answer_text for phrase in generic_phrases)

        if contains_generic_phrase_final:
            print("\nGPT-4 was too generic, Doing google search")
            do_google_fallback()
        else:
            print("\n Weaviate-based Answer:")
            print(final_answer.content)

            #Only Unique Titles
            unique_titles = set(doc.metadata['video_title'] for doc in docs)
            print("\n Kaynaklar:")
            for title in unique_titles:
                print(f"- {title}")

finally:
    client.close()
