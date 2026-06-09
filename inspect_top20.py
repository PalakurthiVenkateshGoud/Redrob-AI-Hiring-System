# inspect_top20.py

from parser import load_candidates

TARGETS = {
    "CAND_0079064",
    "CAND_0079387",
    "CAND_0028793",
    "CAND_0083307",
    "CAND_0005649"
}

candidates = load_candidates()

for c in candidates:

    if c["candidate_id"] in TARGETS:

        print("\n" + "="*80)
        print(c["candidate_id"])
        print(c["profile"]["current_title"])
        print(c["profile"]["years_of_experience"])

        print("\nSUMMARY:")
        print(c["profile"]["summary"][:800])

        print("\nCAREER:")

        for job in c["career_history"]:

            print("\n-", job["title"], "@", job["company"])
            print(job["description"][:500])