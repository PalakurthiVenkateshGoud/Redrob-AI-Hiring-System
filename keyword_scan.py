import json

keywords = [
    "retrieval",
    "ranking",
    "recommendation",
    "embedding",
    "vector",
    "search",
    "faiss",
    "milvus",
    "pinecone",
    "qdrant",
    "weaviate"
]

counts = {k: 0 for k in keywords}

path = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        text = (
            c["profile"]["summary"] + " " +
            " ".join(job["description"] for job in c["career_history"])
        ).lower()

        for k in keywords:
            if k in text:
                counts[k] += 1

print("\nKeyword Counts:\n")

for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{k}: {v}")