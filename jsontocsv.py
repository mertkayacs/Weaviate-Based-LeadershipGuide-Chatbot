import json
import pandas as pd

# JSON'dan CSV'ye dönüştür
with open("turkish_chunks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_csv("turkish_chunks.csv", index=False)
