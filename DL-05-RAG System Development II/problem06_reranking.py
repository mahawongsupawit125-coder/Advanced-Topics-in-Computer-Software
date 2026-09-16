# -*- coding: utf-8 -*-
# Problem 06: The Relevant Document ends up ranked near the bottom by First-stage Retrieval
# Uses real data from fitness_q_a.txt (nutrition & fitness category)
import sys
from data_loader import load_qa

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")

GENERIC_TERMS = ["โปรตีน", "กล้ามเนื้อ"]
SPECIFIC_TERMS = ["เวย์", "Isolate", "ดูดซึม"]


def first_stage(doc):
    text = doc["question"] + doc["answer"]
    return sum(t in text for t in GENERIC_TERMS)


def rerank(doc):
    text = doc["question"] + doc["answer"]
    score = first_stage(doc)
    score += sum(3 for t in SPECIFIC_TERMS if t in text)
    return score


def run():
    data = load_qa()

    first = sorted(data, key=first_stage, reverse=True)[:6]
    second = sorted(first, key=rerank, reverse=True)

    print("Before Re-ranking (Top 6 from First-stage: generic terms 'โปรตีน','กล้ามเนื้อ'):")
    for d in first:
        print(f"  score={first_stage(d)} | {d['question']}")

    print("\nAfter Re-ranking (extra weight for specific terms, e.g. 'เวย์', 'Isolate'):")
    for d in second:
        print(f"  score={rerank(d)} | {d['question']}")

    print("\nCause: First-stage Retrieval weighs generic terms equally, so the document that is most")
    print("specific and best matches the query can end up ranked near the bottom")
    print("Re-ranking uses finer-grained signals to push the relevant document toward the top")


if __name__ == "__main__":
    run()
