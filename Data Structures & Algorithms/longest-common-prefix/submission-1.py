# 📌 Problem: Longest Common Prefix
# 🎯 Goal: Given a list of strings, find the longest common prefix shared among all strings.

# ✅ Engineering Method:

# 1. Explore:
#    - Input: List of strings (e.g., ["flower", "flow", "flight"])
#    - Output: Longest common prefix (e.g., "fl")
#    - Constraints: If there is no common prefix, return ""

# 2. Brainstorm:
#    - Sorting brings lexicographically smallest and largest strings to the front and back
#    - The common prefix of the first and last strings is the common prefix of the entire list

# 3. Plan:
#    - Sort the list of strings
#    - Compare characters of the first and last strings until a mismatch
#    - Return the matched prefix

# 4. Implement:
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        res = ""

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            res += first[i]

        return res

# 5. Verify:
# Example:
#   Input: ["flower", "flow", "flight"]
#   Output: "fl"

# 6. Time & Space Complexity:
# ⏱ Time Complexity: O(n log n + m), where n is number of strings, m is length of shortest string
# 🧠 Space Complexity: O(1) additional space

# 🔐 Edge Cases:
# - Empty list: return ""
# - No common prefix: return ""
# - All strings identical: return full string

# ✅ Summary:
# Elegant approach using sorting. Good trade-off between simplicity and performance for interview settings.
