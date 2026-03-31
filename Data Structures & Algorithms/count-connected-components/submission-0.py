class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        self.count = 0 



        visited = [False]*n
        adjl = defaultdict(list)

        for src, dst in edges:
            adjl[src].append(dst)
            adjl[dst].append(src)


        def dfs(node):

            visited[node]= True

            for nbr in adjl[node]:
                if not visited[nbr]:
                    dfs(nbr)

        

        for i in range(n):
            if not visited[i]:
                dfs(i)
                self.count+=1
        

        return self.count

        