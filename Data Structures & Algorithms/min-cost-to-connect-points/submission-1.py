from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjl = defaultdict(list)
        for index, point in enumerate(points):

            for i in range(index+1,len(points)):

                dist = abs(point[0]-points[i][0])  + abs(point[1]-points[i][1])
                adjl[index].append((i,dist))
                adjl[i].append((index,dist))

        visited = set()
        minheap = [(0, 0)]  # (weight, node, parent)
        mst_weight = 0

        while len(visited) < len(points):
            weight, node = heappop(minheap)
            if node in visited:
                continue
            mst_weight += weight
            visited.add(node)

            for nbr, w in adjl[node]:
                if nbr not in visited:
                    heappush(minheap, (w, nbr))

        return mst_weight
