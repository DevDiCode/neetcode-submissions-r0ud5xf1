class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        freq = defaultdict(int)
        freq[0] = 1
        cur = count = 0
        for num in nums:
            cur += num
            count += freq[cur - k]
            freq[cur] += 1
        return count
