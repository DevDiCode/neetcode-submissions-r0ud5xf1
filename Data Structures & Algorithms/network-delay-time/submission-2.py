"""
LC743
https://leetcode.com/problems/network-delay-time/
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
"""
import sys
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        result = [sys.maxsize] * (n + 1)

        adjl = defaultdict(list)

        for u, v, w in times:
            adjl[u].append((v, w))

        minheap = []
        minheap.append((0, k))
        result[k] = 0

        while minheap:
            time, node = heapq.heappop(minheap)

            if time > result[node]:
                continue

            for nbr, nbr_time in adjl[node]:

                if time + nbr_time < result[nbr]:
                    result[nbr] = time + nbr_time
                    heapq.heappush(minheap, (time + nbr_time, nbr))

        response = -sys.maxsize - 1

        for val in result[1::]:
            if val == sys.maxsize:
                return -1
            response = max(response, val)

        return response
