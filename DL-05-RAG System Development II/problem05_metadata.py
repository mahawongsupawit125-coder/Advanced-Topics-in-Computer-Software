# -*- coding: utf-8 -*-
# Problem 05: Similarity Search returns a document with matching text but wrong Metadata (category)
# Uses real data from fitness_q_a.txt
import sys
from data_loader import load_qa

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")

QUERY = "กิน เวย์ โปรตีน เวลา ไหน ดี"
TARGET_CATEGORY = "โภชนาการและอาหารเสริม"


def score(query, text):
    return sum(word in text for word in query.split())


def search(data, query, category=None):
    docs = data if category is None else [d for d in data if d["category"] == category]
    return max(docs, key=lambda d: score(query, d["question"] + " " + d["answer"]))


def run():
    data = load_qa()

    unfiltered = search(data, QUERY)
    filtered = search(data, QUERY, category=TARGET_CATEGORY)

    print("Query:", QUERY)
    print("\nWithout filtering by Metadata (category) -> picks the document with keyword matches across any category:")
    print(f"  [{unfiltered['category']}] {unfiltered['question']}")

    print(f"\nFiltered by Metadata (category='{TARGET_CATEGORY}'):")
    print(f"  [{filtered['category']}] {filtered['question']}")

    print("\nCause: Keyword/Semantic Similarity picks the document with the most matching words")
    print("but does not guarantee the document has the correct Metadata (e.g. specific domain category) the system needs")


if __name__ == "__main__":
    run()
