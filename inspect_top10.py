# inspect_top10.py

from parser import load_candidates

ids = [
"CAND_0083307",
"CAND_0079387",
"CAND_0028793",
"CAND_0030953",
"CAND_0044883"
]

candidates = load_candidates()

for c in candidates:

    if c["candidate_id"] in ids:

        print("\n" + "="*80)
        print(c["candidate_id"])
        print(c["profile"]["current_title"])
        print(c["profile"]["summary"][:1000])

        print("\nCAREER\n")

        for job in c["career_history"][:3]:

            print(job["title"])
            print(job["description"][:500])
            print()