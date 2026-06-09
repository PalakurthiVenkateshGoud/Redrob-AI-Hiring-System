import json

path = r"[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(path, "r", encoding="utf-8") as f:
    for i in range(5):
        c = json.loads(next(f))

        print("\n" + "=" * 80)

        print("ID:", c["candidate_id"])
        print("Title:", c["profile"]["current_title"])
        print("Experience:", c["profile"]["years_of_experience"])

        skills = [s["name"] for s in c["skills"][:10]]
        print("Skills:", skills)

        print("Response Rate:",
              c["redrob_signals"]["recruiter_response_rate"])

        print("Github:",
              c["redrob_signals"]["github_activity_score"])