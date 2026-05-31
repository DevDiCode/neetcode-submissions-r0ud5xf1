class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj_list = defaultdict(list)


        for course, pre in prerequisites:

            adj_list[pre].append(course)
        

        lookup = [0]*numCourses

        

        def dfs(node):

            if lookup[node]==1:
                return True
            
            if lookup[node]==2:
                return False
            
            lookup[node] =1

            for neighbor in adj_list[node]:
                
                if dfs(neighbor):
                    return True
            

            lookup[node]=2

            return False
        

        for i in range(numCourses):

            if dfs(i):
                return False
        

        return True



