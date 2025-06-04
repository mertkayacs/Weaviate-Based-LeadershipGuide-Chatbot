import weaviate
import json
from weaviate.classes.config import Property, DataType

# Connect to Docker (Weaviate)
client = weaviate.connect_to_local()

collection_name = "LeadershipContent"

# Does the collection exists?
if collection_name not in client.collections.list_all():
    # Define properties for the collection
    properties = [
        Property(name="video_title", data_type=DataType.TEXT),
        Property(name="chunk", data_type=DataType.TEXT),
        Property(name="source_url", data_type=DataType.TEXT)
    ]

    # Create Collection
    client.collections.create(
        name=collection_name,
        properties=properties
    )
    print(f"✅ Created collection: {collection_name}")
else:
    print(f"ℹ️ Collection '{collection_name}' already exists!")

# Loading chunks from json
with open("turkish_chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Accessing the collection
collection = client.collections.get(collection_name)

# Chunk to Weaviate
for idx, chunk_data in enumerate(chunks):
    data_object = {
        "video_title": chunk_data["video_title"],
        "chunk": chunk_data["chunk"],
        "source_url": chunk_data["source_url"]
    }
    collection.data.insert(data_object)
    if (idx + 1) % 50 == 0 or (idx + 1) == len(chunks):
        print(f"🔄 Uploaded {idx + 1}/{len(chunks)} chunks...")

print("\n✅ All chunks uploaded to Weaviate!")

client.close()
