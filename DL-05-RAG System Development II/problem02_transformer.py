# -*- coding: utf-8 -*-
# Problem 02: Vocabulary Mismatch (formal vs slang) and Token order (Position)
# Uses real questions from fitness_q_a.txt
import sys
from data_loader import load_qa

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")


def bow(text):
    result = {}
    for token in text.split():
        result[token] = result.get(token, 0) + 1
    return result


def with_position(text):
    return [(i, token) for i, token in enumerate(text.split())]


def find_pair(data):
    formal = next((d for d in data if "เวทเทรนนิ่ง" in d["question"]), data[0])
    slang = {
        "question": "เล่นเวท เพื่อ สร้าง กล้ามเนื้อ ควร เริ่ม อย่างไร",
        "answer": formal["answer"],
        "lang": "แสลง"
    }
    return formal, slang


def run():
    data = load_qa()
    formal, slang = find_pair(data)

    print("Formal-register question:", formal["question"])
    print("Slang-register question :", slang["question"])
    print("BoW (formal):", bow(formal["question"]))
    print("BoW (slang) :", bow(slang["question"]))
    common = set(bow(formal["question"])) & set(bow(slang["question"]))
    print("Exact-token overlap:", common or "None")
    print("-> Both questions are about the same topic (starting weight training for muscle growth)")
    print("   but Keyword/BoW barely overlaps because the wording differs (Vocabulary Mismatch)")

    print("\nExample: effect of Token order on meaning (Position):")
    # Use the answer instead of the question, since the question is too short
    # (not enough whitespace-separated tokens to show the effect of reordering)
    a = " ".join(formal["answer"].split()[:8])
    b = " ".join(reversed(a.split()))
    print("A (original):", with_position(a))
    print("B (reversed order):", with_position(b))
    print("BoW identical:", bow(a) == bow(b))

    print("\nCause: BoW does not capture vocabulary variation and does not preserve word order")
    print("Transformers use Positional Information + Self-Attention and semantic Embeddings")
    print("to match questions that use different wording but share the same intent (e.g. formal vs slang)")


if __name__ == "__main__":
    run()
