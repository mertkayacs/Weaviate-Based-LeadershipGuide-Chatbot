# 🧠 Advanced AI Chatbot with Weaviate, HuggingFace, and GPT-4

This project was my deep-dive into crafting a smart, context-aware chatbot using powerful modern tools like **Weaviate**, **HuggingFace Embeddings**, and **GPT-4**. Unlike the lightweight Google-fallback variant, this version leverages a full local vector store and context-aware conversation.

---

## 🔍 About

This chatbot is built with:

- **Weaviate** as a vector database
- **HuggingFace** for sentence embeddings
- **LangChain** to manage prompts and context
- **OpenAI GPT-4** as the primary model
- **Google Search Fallback** when Weaviate yields no relevant results
- **Streamlit** for interactive UI

---

## 🚧 Deployment

> ⚠️ Due to high operational costs and dependency complexity (e.g., maintaining Weaviate and local inference), this version has not been deployed to the public.

However, the architecture and modular logic remain reusable and insightful for:

- Large-scale document Q&A bots
- Internal search assistants
- RAG (Retrieval-Augmented Generation) systems

---

## 📁 Structure

```
ai-chatbot-weaviate/
├── app.py                    # Streamlit UI
├── weaviate_client.py        # Handles vector DB ops
├── embedding.py              # HuggingFace embedding wrapper
├── fallback_google.py        # Google search fallback logic
├── prompts/                  # Custom LangChain prompts
└── data/                     # JSON chunks & embeddings
```

---

## 🧠 What It Does

- Accepts a query
- Searches Weaviate for context
- If context is relevant → answer with GPT-4 using that
- If not → fallback to Google, summarize the result
- All served from a clean, styled Streamlit UI

---

## 🛠 Technologies Used

- [Weaviate](https://weaviate.io/)
- [LangChain](https://www.langchain.com/)
- [HuggingFace Transformers](https://huggingface.co/)
- [OpenAI GPT-4](https://openai.com/gpt)
- [Streamlit](https://streamlit.io/)

---

## 📌 Future Goals

- Integrate login/auth
- Deploy on cloud with cost optimization
- Dynamic memory for long conversations
- Fully offline support using local LLMs (e.g., LLaMA or Mistral)

---

## 🙏 Acknowledgements

Huge thanks to the open-source communities behind these tools, and to anyone passionate about making AI practical and usable.

—
Mert Kaya
