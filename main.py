from parser import load_candidates
from scorer import final_score
import csv

candidates = load_candidates()

results = []

for c in candidates:
    score = final_score(c)

    results.append(
    (
        score,
        c["candidate_id"],
        c["profile"]["current_title"],
        c
    )
    )

results.sort(
    key=lambda x: (-x[0], x[1])
)

top_100 = results[:100]

print("\nTOP 20 CANDIDATES\n")

for row in top_100[:20]:
    print(row[:3])

with open("outputs/submission.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, row in enumerate(top_100, start=1):

        score, candidate_id, title, candidate = row

        exp = candidate["profile"]["years_of_experience"]

        writer.writerow([
            candidate_id,
            rank,
            round(score, 4),
            f"{title} with {exp} years of experience and strong alignment to retrieval, ranking and recommendation systems."
        ])

print("\nSubmission file created!")