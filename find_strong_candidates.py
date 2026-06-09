import json

keywords = ["retrieval", "ranking", "recommendation", "embedding"]

path = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

found = 0

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        text = (
            c["profile"]["summary"] + " " +
            " ".join(job["description"] for job in c["career_history"])
        ).lower()

        if any(k in text for k in keywords):

            print("\n" + "=" * 80)
            print("ID:", c["candidate_id"])
            print("Title:", c["profile"]["current_title"])
            print("Experience:", c["profile"]["years_of_experience"])

            print("\nSummary:")
            print(c["profile"]["summary"][:500])

            found += 1

            if found == 10:
                break