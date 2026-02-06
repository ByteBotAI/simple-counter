#!/usr/bin/env python3
"""A simple CLI counter utility."""

import argparse
import json
import os
from pathlib import Path

DATA_FILE = Path.home() / ".counter.json"


def load_count():
    """Load the current count from file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data.get("count", 0)
    return 0


def save_count(count):
    """Save the count to file."""
    with open(DATA_FILE, "w") as f:
        json.dump({"count": count}, f)


def main():
    parser = argparse.ArgumentParser(description="A simple CLI counter")
    parser.add_argument(
        "action",
        choices=["show", "up", "down", "reset"],
        default="show",
        nargs="?",
        help="Action to perform (default: show)",
    )
    parser.add_argument(
        "-n", "--number", type=int, default=1, help="Amount to increment/decrement"
    )

    args = parser.parse_args()

    count = load_count()

    if args.action == "show":
        print(f"Current count: {count}")
    elif args.action == "up":
        count += args.number
        save_count(count)
        print(f"Count increased by {args.number}. New count: {count}")
    elif args.action == "down":
        count -= args.number
        save_count(count)
        print(f"Count decreased by {args.number}. New count: {count}")
    elif args.action == "reset":
        save_count(0)
        print("Count reset to 0")


if __name__ == "__main__":
    main()
