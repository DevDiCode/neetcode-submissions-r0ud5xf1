class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjl = defaultdict(list)

        lookup = [False]*n

        response = 0 

        for src, dst in edges:
            adjl[src].append(dst)
            adjl[dst].append(src)

        def dfs(node):
            
            lookup[node]= True

            for nbr in adjl[node]:
                if not lookup[nbr]:
                    dfs(nbr)


        for i in range(n):

            if lookup[i]==False:
                dfs(i)
                response+=1
        
        return response