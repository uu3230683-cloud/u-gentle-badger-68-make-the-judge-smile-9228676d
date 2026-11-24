"""Write one line about a small good thing that happened today."""

import os

LINE = (
    "At 7:40 this morning the lift doors opened and my neighbour's "
    "toddler, in a full superhero cape, solemnly handed me a single "
    "grape - a toll, he said, for the ride down. I paid it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
