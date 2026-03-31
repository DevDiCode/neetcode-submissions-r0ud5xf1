# Problem 5: Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# 🧠 Pattern: HashMap → Group by Signature Key
# Group all words that are anagrams using a common hashable key.

# ------------------------------
# ✅ Step 1: Explore
# ------------------------------
# Input: List of strings
# Output: List of lists, where each sublist contains grouped anagrams
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# Constraints:
# - All strings are lowercase
# - Length of each string ≤ 100
# - List length ≤ 10⁴

# ------------------------------
# ✅ Step 2: Brainstorm
# ------------------------------
# ❌ Brute force: Compare every pair to check if they’re anagrams → O(n² * k log k)
# ✅ Optimized:
#   - Use a dictionary to group words
#   - Key = sorted version of the word → same for all anagrams
#   - Value = list of words with that key

# Alternative idea:
# - Use a tuple of 26-letter frequencies instead of sorted string
#   - Slightly faster in large cases, but sorting is simpler and sufficient

# ------------------------------
# ✅ Step 3: Plan (Pseudocode)
# ------------------------------
# Initialize hashmap (defaultdict of list)
# For each word in input list:
#   - Sort the word → use as key
#   - Append the word to hashmap[key]
# Return hashmap.values() as list of grouped anagrams

# ------------------------------
# ✅ Step 4: Implement
# ------------------------------
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))  # or use tuple(sorted(word))
            anagram_map[key].append(word)
        return list(anagram_map.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lookup = defaultdict(list)

        for word in strs:

            word_hash = [0] * 26

            for letter in word:
                word_hash[ord(letter) - ord("a")] += 1

            lookup[tuple(word_hash)].append(word)

        return list(lookup.values())

# ------------------------------
# ✅ Step 5: Verify
# ------------------------------
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# Order doesn’t matter

# ------------------------------
# ✅ Step 6: Reflect
# ------------------------------
# Pattern: Group-by Key → HashMap
# Key Insight: Anagrams share sorted character order
# Time: O(n * k log k) — n = number of words, k = max length of word
# Space: O(nk)
