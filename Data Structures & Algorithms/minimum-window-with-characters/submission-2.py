"""
LeetCode 76 – Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/  [file:1]

Engineering method:

Problem:
    Given two strings s and t, return the minimum window substring of s such that
    every character in t (including duplicates) is included in the window.
    If no such substring exists, return "". [file:1]

Pattern:
    Sliding window – "cover all required characters" / pattern matching:
    - Expand right pointer to include chars until all requirements from t are met.
    - Once window is valid, shrink from left to make it minimal. [file:1]

Key ideas:
    - Use two hash maps:
        need[c]   -> frequency of c required (from t)
        window[c] -> frequency of c in current window [L, R] [file:1]
    - have: how many distinct chars currently satisfy window[c] >= need[c]
    - needCount: total distinct chars in t
    - A window is valid when have == needCount. [file:1]

Complexity:
    - Time: O(len(s) + len(t)), each char enters/exits window at most once. [file:1]
    - Space: O(U) where U is number of distinct chars in s ∪ t (bounded by ASCII/Unicode set used). [file:1]
"""

from collections import Counter
from typing import Dict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if not t or not s:
            return ""

        need: Dict[str, int] = Counter(t)   # required frequencies
        window: Dict[str, int] = {}

        needCount = len(need)  # number of distinct chars we need to satisfy
        have = 0               # number of distinct chars satisfied in window

        L = 0
        min_len = float("inf")
        min_start = 0

        for R, ch in enumerate(s):
            # Expand window: include s[R]
            window[ch] = window.get(ch, 0) + 1

            # If this character is required and we just met its required count, update have
            if ch in need and window[ch] == need[ch]:
                have += 1

            # When window is valid, try to shrink from the left
            while have == needCount:
                window_len = R - L + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = L

                # Shrink: remove s[L] from window
                left_char = s[L]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                L += 1

        return "" if min_len == float("inf") else s[min_start:min_start + min_len]
