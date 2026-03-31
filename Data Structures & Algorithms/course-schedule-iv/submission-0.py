# Course Prerequisite Checking (LeetCode 1462)
#
# Engineering Method
#
# Exploration
# Given numCourses, a list of prerequisite edges [a, b] ("take a before b") and queries [u, v], check for each if u is an indirect (or direct) prerequisite of v.
#
# Brainstorm
# - Transitive prerequisite checking = reachability in directed graph.
# - For each node, use DFS to mark all courses reachable from it.
# - Alternatively, Floyd-Warshall or BFS works but DFS fits with adjacency list efficiently due to sparse graphs and small course counts.
#
# Plan
# - Build adjacency list adj[pre] = [course,...]
# - For each course, compute reachable matrix using DFS (reachable[i][j]: i can reach j).
# - For each query [u, v], answer reachable[u][v].
#
# Implementation

from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, course in prerequisites:
            adj[pre].append(course)

        reachable = [[False] * numCourses for _ in range(numCourses)]

        def dfs(start: int, node: int):
            for nei in adj[node]:
                if not reachable[start][nei]:
                    reachable[start][nei] = True
                    dfs(start, nei)

        for i in range(numCourses):
            dfs(i, i)

        return [reachable[u][v] for u, v in queries]

# Edge Cases
# - No prerequisites: all queries return False
# - Cycle: handled naturally
# - Disconnected graph: returns False for unreachable pairs

# Time and Space Complexity
# - Time: O(N^3) worst-case (N^2 DFS traversals up to N per call)
# - Space: O(N^2) for reachable matrix and up to O(N) for recursion stack
