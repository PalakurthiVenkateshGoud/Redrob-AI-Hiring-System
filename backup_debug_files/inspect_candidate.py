# inspect_candidate.py

import json

TARGET = "CAND_0000024"

path = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        if c["candidate_id"] == TARGET:
            print(json.dumps(c, indent=2))
            break