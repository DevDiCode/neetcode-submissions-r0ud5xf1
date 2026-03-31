# DSA Note: Connected Components in Undirected Graph (Leetcode 323)
# ---------------------------------------------------------------
# Task: Count number of connected components (groups of connected nodes).
# Input: 
#   - n: total nodes (0 to n-1)
#   - edges: list of [u, v] pairs (undirected)
#
# Edge Cases:
#   - n == 0 => Output 0
#   - edges == [] => Each node is its own component, output n
#   - Self-loops or duplicate edges: no effect
#   - n == 1 => Output 1
#
# Steps:
#   1. Build adjacency list
#   2. Use DFS to visit all nodes in a component
#   3. Count DFS triggers (each is a new component)
#
# ---------------------------------------------------------------
from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjl = defaultdict(list)
        for u, v in edges:
            adjl[u].append(v)
            adjl[v].append(u)
        visited = [False] * n
        def dfs(node):
            visited[node] = True
            for nei in adjl[node]:
                if not visited[nei]:
                    dfs(nei)
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

# Complexity:
#   - Time: O(n + E), each node and edge is visited
#   - Space: O(n + E), adjacency list + visited array
