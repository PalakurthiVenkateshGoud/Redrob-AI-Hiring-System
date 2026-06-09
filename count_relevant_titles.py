import json
from collections import Counter

relevant = Counter()

keywords = [
    "retrieval",
    "ranking",
    "recommendation",
    "embedding"
]

path = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        text = (
            c["profile"]["summary"] + " " +
            " ".join(job["description"] for job in c["career_history"])
        ).lower()

        if any(k in text for k in keywords):
            relevant[c["profile"]["current_title"]] += 1

for title, count in relevant.most_common(30):
    print(f"{title}: {count}")