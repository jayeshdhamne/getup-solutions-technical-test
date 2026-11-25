"""Simple internal policy Q&A script for disability services staff."""

import json
import re

POLICIES = [
    {
        "id": "P01",
        "text": "A coordinator must approve a roster change before it takes effect.",
    },
    {
        "id": "P02",
        "text": "Staff must record an incident in the incident register before the end of the shift.",
    },
]

FALLBACK_ANSWER = (
    "Sorry, I could not find an answer to that question in the available internal policies."
)

# Common words to ignore so generic words do not cause wrong matches
STOP_WORDS = {
    "a", "an", "and", "are", "at", "be", "before", "by", "can", "do",
    "for", "from", "how", "i", "in", "is", "it", "much", "must", "of",
    "on", "or", "should", "staff", "takes", "the", "to", "what", "when",
    "where", "who", "why",
}


def get_keywords(text):
    """Turn text into a set of simple lowercase keywords."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    keywords = set()
    for word in words:
        if word in STOP_WORDS:
            continue
        # Handle simple plurals/verbs like "approves" -> "approve"
        if len(word) > 3 and word.endswith("s"):
            word = word[:-1]
        keywords.add(word)
    return keywords


def answer_question(question):
    """Find the best matching policy and return the answer with source IDs."""
    if not question or not question.strip():
        return {"answer": FALLBACK_ANSWER, "source_ids": []}

    question_keywords = get_keywords(question)
    best_policy = None
    best_score = 0

    for policy in POLICIES:
        policy_keywords = get_keywords(policy["text"])
        matches = len(question_keywords & policy_keywords)
        if matches > best_score:
            best_score = matches
            best_policy = policy

    # Require at least 2 matching keywords so unrelated questions fall back safely
    if best_policy is None or best_score < 2:
        return {"answer": FALLBACK_ANSWER, "source_ids": []}

    return {
        "answer": f"{best_policy['text']} (Source: {best_policy['id']})",
        "source_ids": [best_policy["id"]],
    }


if __name__ == "__main__":
    checks = [
        "Who approves a roster change?",
        "When should I record an incident?",
        "How much can staff claim for travel?",
    ]
    for q in checks:
        result = answer_question(q)
        print(f"Question: {q}")
        print(json.dumps(result, indent=2))
        print()
