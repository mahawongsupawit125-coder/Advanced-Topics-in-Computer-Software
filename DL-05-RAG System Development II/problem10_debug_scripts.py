# -*- coding: utf-8 -*-
# Problem 10: Debug RAG Scripts & Pipeline Inspection
# Demonstrates how to inspect data loading, chunking, and metadata consistency for debugging.
import sys
from data_loader import load_qa

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")


def run():
    data = load_qa()
    print("=== Problem 10: Debug RAG Scripts ===")
    print(f"Total entries loaded: {len(data)}")
    if data:
        print("\nSample Entry Inspection (ID 0):")
        for key, val in data[0].items():
            if key == "answer" and len(str(val)) > 100:
                print(f"  {key:10s}: {val[:100]}...")
            else:
                print(f"  {key:10s}: {val}")

    print("\nDebugging Checkpoints:")
    print("1. Data Integrity    : Verify Q&A format and mandatory fields (category, question, answer)")
    print("2. Text Normalization: Check character encoding and space normalization")
    print("3. Vector Store Sync : Ensure index entries match source document IDs")


if __name__ == "__main__":
    run()
