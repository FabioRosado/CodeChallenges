"""
Given a word and a list of possible anagrams, select the correct sublist.

Given `"listen"` and a list of candidates like `"enlists" "google"
"inlets" "banana"` the program should return a list containing
`"inlets"`.
"""
from collections import Counter


def detect_anagrams(word, candidates):
    """Detect if a candidate is an anagram of word """
    return [candidate for candidate in candidates
            if Counter(word.lower()) == Counter(candidate.lower())
            and word.lower() != candidate.lower()]
