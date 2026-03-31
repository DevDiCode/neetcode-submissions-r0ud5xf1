# Redundant Connection (LeetCode 684)
#
# Engineering Method
#
# Exploration
# Given a list of edges for an undirected graph, where all nodes are connected and it's almost a tree except for one extra edge.
# Return the edge that, if removed, results in a tree (i.e., the edge that creates a cycle).
#
# Brainstorm
# - Use DSU (Union-Find): For each edge, check if the two nodes are already in the same set.
# - If adding the edge connects two nodes already in the same component, it's redundant.
#
# Plan
# - Initialize DSU for n nodes.
# - For each edge [u, v]:
#     - If union(u, v) returns False (already connected), return [u, v] (redundant edge).
#     - Else, union(u, v).
# - Return the redundant edge.

from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))  # node labels from 1 to n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False  # cycle detected
        self.parent[yr] = xr
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        return []

# Edge Cases
# - Only one edge: never redundant
# - Multiple possible redundant edges: return the last one in input order (per problem statement)
#
# Time and Space Complexity
# - Time: O(n*α(n)), where n is number of nodes, α is inverse Ackermann (nearly constant)
# - Space: O(n) for DSU arrays
