import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        adj = defaultdict(list)



        for i , val in enumerate(points):

            node = i 
            x1, y1 = val 

            for j in range(i+1,len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist,j))
                adj[j].append((dist,i))

        total_cost = 0 
        n = len(points)
        lookup = [False]*n

        q = []

        q.append((0,0,0))

        while q :
            wt, node, parent = heapq.heappop(q)

            if lookup[node]:
                continue
            lookup[node]= True
            total_cost+=wt

            for dist, nb in adj[node]:
                if not lookup[nb]:
                    heapq.heappush(q,(dist,nb,node))
        


        return total_cost



        
        