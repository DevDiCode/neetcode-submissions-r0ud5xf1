class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        N = numCourses
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        lookup = [0] * N  # 0 = unvisited, 1 = visiting, 2 = visited


        def dfs(node):
            if lookup[node] == 1:  # If the node is being visited, cycle detected
                return True

            # if lookup[node] == 2:  # Already processed node, no cycle
            #     return False

            lookup[node] = 1  # Mark node as visiting

            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True

            lookup[node] = 2  # Mark node as fully processed
            return False

        # Check for each node if a cycle is present
        for i in range(N):
            if lookup[i] == 0:  # Not visited yet
                if dfs(i):
                    return False

        return True
