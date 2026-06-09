from collections import Counter
import csv

counter = Counter()

with open("outputs/submission.csv") as f:

    next(f)

    ids = set()

    for line in f:
        ids.add(line.split(",")[0])

# load candidates

from parser import load_candidates

candidates = load_candidates()

for c in candidates:

    if c["candidate_id"] in ids:

        counter[c["profile"]["current_title"]] += 1

print(counter.most_common(20))