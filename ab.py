import json

count = 0

with open(r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:
    for _ in f:
        count += 1

print("Candidates:", count)