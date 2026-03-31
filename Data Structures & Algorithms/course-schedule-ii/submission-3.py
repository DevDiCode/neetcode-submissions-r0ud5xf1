class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        response = []


        adj = defaultdict(list)


        for course , pre in  prerequisites:
            adj[course].append(pre)
        


        def dfs(course):

            if lookup[course] == 1:  # Cycle detected
                return True
            if lookup[course] == 2:  # Already processed
                return False

            # Mark as visiting
            lookup[course] = 1

            # Process all prerequisites
            for pre in adj[course]:
                if dfs(pre):
                    return True
                
            lookup[course]=2
            response.append(course)

            return False
            # Mark as visiting
        

        lookup = [0]*numCourses


        for i in range(numCourses):
            if lookup[i]==0:
                if dfs(i):
                    return []
        
        return response