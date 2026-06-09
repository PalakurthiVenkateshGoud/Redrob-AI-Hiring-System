import json

DATA_PATH = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"


def load_candidates(limit=None):
    candidates = []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if limit and i >= limit:
                break

            candidates.append(json.loads(line))

    return candidates


if __name__ == "__main__":
    candidates = load_candidates(5)

    print("Loaded:", len(candidates))

    for c in candidates:
        print(
            c["candidate_id"],
            c["profile"]["current_title"],
            c["profile"]["years_of_experience"]
        )