import json

path = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(path, "r", encoding="utf-8") as f:
    for i in range(10):
        candidate = json.loads(next(f))

        print("\n" + "=" * 80)
        print("Candidate ID:", candidate["candidate_id"])
        print("Title:", candidate["profile"]["current_title"])
        print("Experience:", candidate["profile"]["years_of_experience"], "years")

        print("\nCareer History:")

        for job in candidate["career_history"]:
            print(f"\n{job['title']} @ {job['company']}")
            print(job["description"][:200])