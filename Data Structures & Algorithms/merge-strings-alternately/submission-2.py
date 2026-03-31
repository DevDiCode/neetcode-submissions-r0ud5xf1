# ✅ Problem: Merge Strings Alternately (Leetcode 1768)
# Given two strings word1 and word2, merge them by alternating characters from each.
# If one string is longer, append the extra characters at the end.

# ---------------------------------------------------------
# 🧠 Pattern: Two Pointers / Simulation
# Alternate between both strings using two indices and append remaining characters.
# ---------------------------------------------------------

# 🔍 Step-by-Step Plan:
# 1. Initialize two pointers for word1 and word2.
# 2. Use a while loop to alternate characters until one string is exhausted.
# 3. Append the remaining characters from the longer string.
# 4. Return the merged result.

# 🧪 Edge Cases:
# - One string is empty → return the other string.
# - Both strings are of unequal length → append extra chars of longer one.
# - Both strings are empty → return "".

# ⏱️ Time Complexity: O(n + m), where n = len(word1), m = len(word2)
# 🔁 Space Complexity: O(n + m) for the result string

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []

        # Step 1: Merge alternately while both strings have characters
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        # Step 2: Append remaining characters from word1 or word2
        if i < len(word1):
            res.append(word1[i:])
        if j < len(word2):
            res.append(word2[j:])

        return ''.join(res)

# ✅ Example Test Cases
sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))      # "apbqcr"
print(sol.mergeAlternately("ab", "pqrs"))      # "apbqrs"
print(sol.mergeAlternately("abcd", "pq"))      # "apbqcd"
