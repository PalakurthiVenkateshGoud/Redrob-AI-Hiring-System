import json

keywords = [
    "retrieval",
    "ranking",
    "recommendation",
    "embedding",
    "evaluation",
    "faiss",
    "pinecone"
]

path = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

matches = []

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        text = (
            c["profile"]["summary"] + " " +
            " ".join(job["description"] for job in c["career_history"])
        ).lower()

        score = sum(1 for k in keywords if k in text)

        if score > 0:
            matches.append(
                (
                    score,
                    c["candidate_id"],
                    c["profile"]["current_title"],
                    c["profile"]["years_of_experience"]
                )
            )

matches.sort(reverse=True)

for row in matches[:20]:
    print(row)