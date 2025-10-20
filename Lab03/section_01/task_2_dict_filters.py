#!/usr/bin/env python3
"""
Lab 3 - Task 2: Build a dictionary from the given animal names and create
three new dictionaries with words containing 'a', 'b', and 'y' (case-insensitive).
How to run:
  python3 task_2_dict_filters.py
"""

animals = [
    "Ferret", "boar", "jaguar", "giraffe", "lizard", "locust", "lion", "wolf",
    "parrot", "raccoon", "butterfly", "jellyfish", "fly", "gnat", "bat", "otter",
    "bear", "polar bear", "oyster", "sheep", "bee", "eagle", "antelope", "spider",
    "squirrel", "tuna", "ostrich", "wasp", "whale", "bison", "buffalo", "owl",
    "donkey", "horse", "goat", "squid", "chameleon", "camel", "crab", "kangaroo",
    "cat", "dog"
]

def build_animals_dict():
    # We'll preserve original capitalization in values and use lowercase keys
    # This makes membership tests case-insensitive and keeps original names.
    return {name.lower(): name for name in animals}

def filter_by_letter(d, letter):
    letter = letter.lower()
    return {k: v for k, v in d.items() if letter in k}

def main():
    d = build_animals_dict()
    a_dict = filter_by_letter(d, "a")
    b_dict = filter_by_letter(d, "b")
    y_dict = filter_by_letter(d, "y")

    print("Original dictionary size:", len(d))
    print("Contains 'a':", len(a_dict), "items ->", sorted(a_dict.values()))
    print("Contains 'b':", len(b_dict), "items ->", sorted(b_dict.values()))
    print("Contains 'y':", len(y_dict), "items ->", sorted(y_dict.values()))

if __name__ == "__main__":
    main()
