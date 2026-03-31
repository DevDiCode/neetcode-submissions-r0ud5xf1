import heapq
from collections import defaultdict
from typing import List

from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjl = defaultdict(list)

        for s, d, price in flights:
            adjl[s].append((d, price))

        minheap = [(0, 0, src)]  # (cost, stops, node)
        visited = dict()  # (node, stops): cost

        while minheap:
            curr_cost, stops, city = heappop(minheap)

            if city == dst:
                return curr_cost

            if stops <= k:
                for nbr, price in adjl[city]:
                    new_cost = curr_cost + price

                    # Only proceed if we haven’t visited or found a cheaper cost
                    if (nbr, stops + 1) not in visited or new_cost < visited[(nbr, stops + 1)]:
                        visited[(nbr, stops + 1)] = new_cost
                        heappush(minheap, (new_cost, stops + 1, nbr))

        return -1