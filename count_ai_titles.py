import json
from collections import Counter

titles = Counter()

path = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)
        titles[c["profile"]["current_title"]] += 1

print("\nTop Titles:\n")

for title, count in titles.most_common(30):
    print(f"{title}: {count}")