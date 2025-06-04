import weaviate

# Connect to local Weaviate
client = weaviate.connect_to_local()

# Access the collection
collection = client.collections.get("LeadershipContent")

# Fetch a few objects
results = collection.query.fetch_objects(limit=5)

# Print them
for obj in results.objects:
    print(f"🎥 Video: {obj.properties['video_title']}")
    print(f"📝 Chunk: {obj.properties['chunk'][:100]}...")  # show first 100 characters
    print(f"🔗 URL: {obj.properties['source_url']}")
    print("-" * 50)

# Close the connection
client.close()
