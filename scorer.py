JD_KEYWORDS = [
    "retrieval",
    "ranking",
    "recommendation",
    "embedding",
    "embeddings",
    "vector database",
    "vector search",
    "faiss",
    "pinecone",
    "qdrant",
    "weaviate",
    "milvus",
    "candidate matching"
]

GOOD_TITLES = [
    "senior ai engineer",
    "ai engineer",
    "applied ml engineer",
    "machine learning engineer",
    "recommendation systems engineer",
    "search engineer",
    "nlp engineer",
    "senior nlp engineer",
    "senior machine learning engineer",
    "senior data scientist",
    "data scientist",
    "ml engineer",
    "ai specialist",
    "ai research engineer",
    "backend engineer",
    "software engineer",
    "data engineer"
]

BAD_TITLES = [
    "hr manager",
    "accountant",
    "content writer",
    "sales executive",
    "graphic designer",
    "marketing manager",
    "customer support",
    "civil engineer"
]


def experience_score(candidate):
    exp = candidate["profile"]["years_of_experience"]

    if 5 <= exp <= 9:
        return 100
    if 4 <= exp < 5:
        return 80
    if 9 < exp <= 12:
        return 70

    return 40


def keyword_score(candidate):
    text = (
        candidate["profile"]["summary"] + " " +
        " ".join(job["description"] for job in candidate["career_history"])
    ).lower()

    score = 0

    for keyword in JD_KEYWORDS:
        if keyword in text:
            score += 15

    return min(score, 100)


def title_score(candidate):

    title = candidate["profile"]["current_title"].lower()

    for bad in BAD_TITLES:
        if bad in title:
            return 0

    if "search engineer" in title:
        return 100

    if "recommendation systems engineer" in title:
        return 100

    if "ai engineer" in title:
        return 95

    if "applied ml engineer" in title:
        return 95

    if "machine learning engineer" in title:
        return 95

    if "nlp engineer" in title:
        return 90

    if "data scientist" in title:
        return 85

    if "backend engineer" in title:
        return 75

    if "software engineer" in title:
        return 75

    if "data engineer" in title:
        return 70

    return 40


def behavior_score(candidate):

    s = candidate["redrob_signals"]

    score = 0

    score += s["recruiter_response_rate"] * 25

    score += s["interview_completion_rate"] * 20

    score += min(
        s["saved_by_recruiters_30d"] * 2,
        15
    )

    score += min(
        s["search_appearance_30d"] / 10,
        10
    )

    score += min(
        s["profile_views_received_30d"] / 10,
        10
    )

    score += min(
        s["profile_completeness_score"] / 5,
        10
    )

    if s["open_to_work_flag"]:
        score += 5

    if s["verified_email"]:
        score += 2.5

    if s["verified_phone"]:
        score += 2.5

    return min(score, 100)

def honeypot_penalty(candidate):

    penalty = 0

    for skill in candidate["skills"]:

        if (
            skill["proficiency"] == "expert"
            and skill.get("duration_months", 0) < 6
        ):
            penalty += 10

    profile = candidate["profile"]

    title = profile["current_title"].lower()

    summary = profile["summary"].lower()

    if (
        any(bad in title for bad in BAD_TITLES)
        and (
            "machine learning" in summary
            or "retrieval" in summary
            or "ranking" in summary
        )
    ):
        penalty += 30

    return penalty

def career_relevance_score(candidate):

    text = " ".join(
        job["description"]
        for job in candidate["career_history"]
    ).lower()

    strong_terms = [
    "retrieval",
    "ranking",
    "recommendation",
    "embedding",
    "embeddings",
    "faiss",
    "pinecone",
    "candidate matching",
    "semantic search",
    "hybrid retrieval",
    "learning-to-rank",
    "bm25",
    "dense retrieval",
    "vector search",
    "re-ranking",
    "xgboost",
    "lightgbm",
    "a/b test",
    "evaluation"
    ]

    score = 0

    for term in strong_terms:
        if term in text:
            score += 15

    return min(score, 100)


def final_score(candidate):

    exp = experience_score(candidate)
    kw = keyword_score(candidate)
    title = title_score(candidate)
    beh = behavior_score(candidate)
    career = career_relevance_score(candidate)

    penalty = honeypot_penalty(candidate)

    score = (
    0.15 * exp +
    0.15 * kw +
    0.15 * title +
    0.40 * career +
    0.15 * beh
)

    score = score - penalty

    return round(score, 2)