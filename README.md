# Weaviate-Based-LeadershipGuide-Chatbot

A Turkish leadership coaching chatbot built as a RAG (retrieval-augmented generation) pipeline. It answers questions from a Weaviate vector store of transcribed leadership videos, with a Google Search fallback when the local content is not relevant, and serves the chat through a Streamlit UI.

## How to Run

The repo ships with the processed data (`turkish_chunks.json`), so the transcription pipeline is optional.

1. Start a local Weaviate instance:

```
docker compose up -d
```

2. Install the Python dependencies:

```
pip install -r requirements.txt
```

3. Set the environment variables used by the app: `OPENAI_API_KEY` for the GPT-4o calls, and `GOOGLE_API_KEY` plus `GOOGLE_CSE_ID` for the Google Search fallback.

4. Create the `LeadershipContent` collection and load the chunks:

```
python upload_to_weaviate.py
```

5. Start the chatbot:

```
streamlit run steamlit_leadership_chatbot.py
```

Optional data pipeline (already done, outputs are in the repo): `audio_downloader.py` downloads a YouTube playlist with yt-dlp, `transcript_maker_whisper.py` transcribes the audio with Whisper, `prepare_transcripts.py` cleans the subtitles into `turkish_chunks.json`, and `jsontocsv.py` converts it to CSV. `chatbot.py` is a command line variant that connects to Weaviate Cloud instead of the local instance (it needs `WEAVIATE_URL` and `WEAVIATE_API_KEY`).

## Tech Used

- Python, Streamlit (UI)
- Weaviate (vector database, local via Docker or Weaviate Cloud)
- LangChain (`langchain-weaviate`, `langchain-openai`, `langchain-huggingface`, `langchain-google-community`)
- OpenAI GPT-4o for relevance checks and answer generation
- HuggingFace sentence-transformers (`paraphrase-multilingual-MiniLM-L12-v2`) for embeddings
- Google Search API as a fallback source
- yt-dlp and OpenAI Whisper for the audio download and transcription pipeline

## Status

Side project, 2025. Not deployed publicly.

## License

Apache License 2.0. See `LICENSE`.
