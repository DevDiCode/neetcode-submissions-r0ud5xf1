# Find the Town Judge (LeetCode 997)
#
# Engineering Method
#
# Exploration
# There are n people labeled from 1 to n. Each trust relationship [a, b] means a trusts b.
# The town judge is trusted by everyone (n-1) but trusts nobody.
#
# Brainstorm
# - Count how many people trust each person (in-degree) and how many each trusts (out-degree).
# - The judge has in-degree = n-1 and out-degree = 0.
#
# Plan
# - Create arrays out_degree and in_degree (size n+1 for 1-indexed labels).
# - Iterate trust list, update out_degree and in_degree.
# - Check for person with out_degree = 0 and in_degree = n-1.
# - Return person or -1 if no judge found.

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degree = [0] * (n + 1)
        in_degree = [0] * (n + 1)
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        for person in range(1, n + 1):
            if out_degree[person] == 0 and in_degree[person] == n - 1:
                return person
        return -1

# Edge Cases
# - n == 1: judge is 1 (no trust needed)
# - No judge: returns -1 if no such person
# - Multiple people trusted by n-1 but one trusts someone: not a judge

# Time and Space Complexity
# - Time: O(T + n), T = len(trust)
# - Space: O(n) for degree arrays


        