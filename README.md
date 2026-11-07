<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/brand/svg/leadershipguide-logo-on-dark.svg">
    <img src="docs/brand/svg/leadershipguide-logo-on-light.svg" alt="LeadershipGuide" width="260">
  </picture>
</p>

<h1 align="center">Leadership coaching in Turkish. Answers from a Weaviate vector store.</h1>

<p align="center">
  A retrieval-augmented leadership chatbot with a Weaviate vector store and a Streamlit interface.<br>
  <b>281 chunks from 27 interviews. GPT-4o. Google fallback. Local Docker or Weaviate Cloud.</b>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-3b82f6?style=flat-square"></a>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
  <img alt="281 transcript chunks" src="https://img.shields.io/badge/chunks-281-2F6B4F?style=flat-square">
  <img alt="Side project, 2025" src="https://img.shields.io/badge/project-side%20project%202025-4F7A63?style=flat-square">
  <a href="https://github.com/mertkayacs/Weaviate-Based-LeadershipGuide-Chatbot"><img alt="GitHub stars" src="https://img.shields.io/github/stars/mertkayacs/Weaviate-Based-LeadershipGuide-Chatbot?style=flat-square&logo=github&color=8A6D3B"></a>
</p>

<p align="center">
  <a href="#quick-start"><img alt="Quick start" src="https://img.shields.io/badge/Quick%20start-4F7A63?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNMTIgMTV2NXMzLjAzLS41NSA0LTJjMS4wOC0xLjYyIDAtNSAwLTUiLz48cGF0aCBkPSJNNC41IDE2LjVjLTEuNSAxLjI2LTIgNS0yIDVzMy43NC0uNSA1LTJjLjcxLS44NC43LTIuMTMtLjA5LTIuOTFhMi4xOCAyLjE4IDAgMCAwLTIuOTEtLjA5Ii8%2BPHBhdGggZD0iTTkgMTJhMjIgMjIgMCAwIDEgMi0zLjk1QTEyLjg4IDEyLjg4IDAgMCAxIDIyIDJjMCAyLjcyLS43OCA3LjUtNiAxMWEyMi40IDIyLjQgMCAwIDEtNCAyeiIvPjxwYXRoIGQ9Ik05IDEySDRzLjU1LTMuMDMgMi00YzEuNjItMS4wOCA1IC4wNSA1IC4wNSIvPjwvZz48L3N2Zz4%3D&logoColor=white"></a>
  <a href="docker-compose.yml"><img alt="Compose file" src="https://img.shields.io/badge/Compose%20file-1E2A38?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNMjIgNy43YzAtLjYtLjQtMS4yLS44LTEuNWwtNi4zLTMuOWExLjcyIDEuNzIgMCAwIDAtMS43IDBsLTEwLjMgNmMtLjUuMi0uOS44LS45IDEuNHY2LjZjMCAuNS40IDEuMi44IDEuNWw2LjMgMy45YTEuNzIgMS43MiAwIDAgMCAxLjcgMGwxMC4zLTZjLjUtLjMuOS0xIC45LTEuNVoiLz48cGF0aCBkPSJNMTAgMjEuOVYxNEwyLjEgOS4xIi8%2BPHBhdGggZD0ibTEwIDE0IDExLjktNi45Ii8%2BPHBhdGggZD0iTTE0IDE5Ljh2LTguMSIvPjxwYXRoIGQ9Ik0xOCAxNy41VjkuNCIvPjwvZz48L3N2Zz4%3D&logoColor=white"></a>
  <a href="https://github.com/mertkayacs/Leadership-Coach-Chatbot"><img alt="Leadership Coach" src="https://img.shields.io/badge/Leadership%20Coach-1E2A38?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNMTUgNmE5IDkgMCAwIDAtOSA5VjMiLz48Y2lyY2xlIGN4PSIxOCIgY3k9IjYiIHI9IjMiLz48Y2lyY2xlIGN4PSI2IiBjeT0iMTgiIHI9IjMiLz48L2c%2BPC9zdmc%2B&logoColor=white"></a>
</p>

LeadershipGuide is a Turkish leadership coaching chatbot built as a retrieval-augmented generation pipeline. It answers from a Weaviate vector store of transcribed leadership interviews, with a Google Search fallback when the stored content does not fit the question. GPT-4o checks relevance and writes the answers, and a Streamlit interface serves the chat. It is the Weaviate variant of the Leadership Coach chatbot.

---

## Why LeadershipGuide

The pipeline keeps the interview chunks in a vector database.

|  |  |
|---|---|
| <img src="docs/assets/readme/icons/database.svg" width="18" height="18" alt=""> **Weaviate store** | The upload script creates a `LeadershipContent` collection and loads 281 chunks from `turkish_chunks.json`. |
| <img src="docs/assets/readme/icons/container.svg" width="18" height="18" alt=""> **Local or cloud** | The Streamlit app uses the local instance from docker-compose.yml. The command line chatbot connects to Weaviate Cloud through `WEAVIATE_URL` and `WEAVIATE_API_KEY`. |
| <img src="docs/assets/readme/icons/languages.svg" width="18" height="18" alt=""> **Multilingual embeddings** | HuggingFace sentence-transformers (paraphrase-multilingual-MiniLM-L12-v2) embed the Turkish chunks and the questions. |

## Features

**Retrieval**

- Weaviate collection with the transcript chunks, queried through LangChain.
- GPT-4o relevance check before answering.
- Google search fallback.

**Data pipeline**

- yt-dlp downloads a YouTube playlist and Whisper transcribes it.
- prepare_transcripts.py cleans the subtitles into the chunks file. The processed data ships in the repository.

## Quick start

```sh
docker compose up -d
pip install -r requirements.txt
python upload_to_weaviate.py
streamlit run steamlit_leadership_chatbot.py
```

Set `OPENAI_API_KEY` for GPT-4o, plus `GOOGLE_API_KEY` and `GOOGLE_CSE_ID` for the Google fallback before starting the app.

The compose file enables anonymous access and binds ports 8080 and 50051 to 127.0.0.1, so Weaviate is reachable from the local machine only.

### Requirements

- Docker with Compose.
- Python with the packages in requirements.txt.
- An OpenAI API key and Google search credentials.

## FAQ

<details>
<summary><b>How is this different from Leadership Coach?</b></summary>

That repository keeps the embeddings in memory and needs no database. This one stores them in Weaviate. See [Leadership-Coach-Chatbot](https://github.com/mertkayacs/Leadership-Coach-Chatbot).
</details>

<details>
<summary><b>Do I have to run the transcription pipeline?</b></summary>

No. The processed chunks are in the repository.
</details>

<details>
<summary><b>Can I use Weaviate Cloud?</b></summary>

The command line variant `chatbot.py` can, with WEAVIATE_URL and WEAVIATE_API_KEY. The Streamlit app uses the local Docker instance.
</details>

If LeadershipGuide is useful to you, a ⭐ helps other people find it.

## License

[Apache License 2.0](LICENSE). See the LICENSE file for the full text.

[![views](https://hits.sh/github.com/mertkayacs/Weaviate-Based-LeadershipGuide-Chatbot.svg?view=today-total&style=flat-square&label=views&color=4F7A63&labelColor=1E2A38)](https://github.com/mertkayacs/Weaviate-Based-LeadershipGuide-Chatbot)
