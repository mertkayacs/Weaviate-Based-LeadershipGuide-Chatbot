import os
import json
import weaviate
from tqdm import tqdm
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from weaviate.collections.classes.config import CollectionConfig, Property, DataType

# --- .env dosyasından API bilgilerini yükle ---
load_dotenv()
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

# --- Weaviate Cloud bağlantısı ---
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
)

# --- Koleksiyon Yapılandırması (Schema) ---
config = CollectionConfig(
    name="LeadershipChunk",
    description="Chunk of leadership content",
    vectorizer="none",  # Dışarıdan vektör veriyoruz
    properties=[
        Property(name="video_title", data_type=DataType.TEXT),
        Property(name="chunk", data_type=DataType.TEXT),
        Property(name="source", data_type=DataType.TEXT),
    ]
)

# --- Koleksiyon varsa oluşturma ---
if "LeadershipChunk" not in client.collections.list_all():
    client.collections.create(config)

# --- HuggingFace Embed Modeli ---
embedder = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# --- Veri Dosyasını Oku ---
with open("turkish_chunks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# --- Koleksiyona Ekleme ---
collection = client.collections.get("LeadershipChunk")

for item in tqdm(data):
    vector = embedder.encode(item["chunk"]).tolist()
    collection.data.insert(
        properties={
            "video_title": item["video_title"],
            "chunk": item["chunk"],
            "source": item["source"]
        },
        vector=vector
    )

# --- Temiz Kapatma ---
print("✅ Veri başarıyla yüklendi.")
client.close()
