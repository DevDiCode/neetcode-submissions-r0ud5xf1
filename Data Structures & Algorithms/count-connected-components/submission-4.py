class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_list = defaultdict(list)


        for source , destination in edges:

            adj_list[source].append(destination)
            adj_list[destination].append(source)
        

        lookup = set()


        connected_components = 0 


        def dfs(node):

            lookup.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in lookup:
                    dfs(neighbor)
            


        for i in range(n):
            if i not in lookup:
                dfs(i)
                connected_components+=1
        


        return connected_components

                    




















