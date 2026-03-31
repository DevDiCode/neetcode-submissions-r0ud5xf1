from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lookup = defaultdict(int)
        threshold = len(nums) // 3 + 1
        result = []

        for val in nums:
            lookup[val] += 1
            if lookup[val] == threshold:
                if val not in result:
                    result.append(val)
            if len(result) == 2:
                break

        return result