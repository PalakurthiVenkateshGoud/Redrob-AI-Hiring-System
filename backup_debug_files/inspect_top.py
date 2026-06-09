from parser import load_candidates
from scorer import final_score

candidates = load_candidates(5000)

results = []

for c in candidates:
    results.append((final_score(c), c))

results.sort(reverse=True, key=lambda x: x[0])

for score, c in results[:3]:
    print("\n" + "="*100)
    print("SCORE:", score)
    print("ID:", c["candidate_id"])
    print("TITLE:", c["profile"]["current_title"])
    print("EXP:", c["profile"]["years_of_experience"])

    print("\nSUMMARY:")
    print(c["profile"]["summary"][:800])

    print("\nCAREER:")
    for job in c["career_history"]:
        print("-", job["title"], "@", job["company"])
        print(job["description"][:300])
        print()