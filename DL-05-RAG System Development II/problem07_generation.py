# -*- coding: utf-8 -*-
# Problem 07: Retrieval is correct, but the Generated Answer distorts the Context (Faithfulness)
# Uses a real answer from fitness_q_a.txt (Weight training frequency & rest window)
import sys
from data_loader import load_qa

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")


def find_entry(data):
    return next((d for d in data if "เล่นเวทเทรนนิ่งกี่วันต่อสัปดาห์" in d["question"]), data[0])


def bad_generator(context):
    # Simulated failure: the generator unknowingly changes a critical number/condition
    return context.replace("48-72 ชั่วโมง", "10 นาที").replace("3 ถึง 5 วัน", "7 วัน วันละ 10 ชั่วโมง")


def grounded_generator(context):
    return context


def run():
    data = load_qa()
    entry = find_entry(data)
    context = entry["answer"]

    print("Question:", entry["question"])
    print("\nRetrieved Context:")
    print(context)

    print("\nBad Generation (distorts the critical rest time and frequency):")
    print(bad_generator(context))

    print("\nGrounded Generation (sticks to the original Context):")
    print(grounded_generator(context))

    print("\nCause: Retrieval is correct, but the Generator changes a critical detail (rest period and training frequency)")
    print("In a fitness & health domain this kind of error can lead to overtraining or injury; the Prompt must force answers to come from Context only")
    print("and Faithfulness must be evaluated before sending the answer to the user")


if __name__ == "__main__":
    run()
