# title_distribution.py

from parser import load_candidates
from scorer import final_score

candidates = load_candidates()

results = []

for c in candidates:
    results.append(
        (
            final_score(c),
            c["profile"]["current_title"]
        )
    )

results.sort(reverse=True)

top100 = results[:100]

counts = {}

for _, title in top100:
    counts[title] = counts.get(title, 0) + 1

for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(k, v)