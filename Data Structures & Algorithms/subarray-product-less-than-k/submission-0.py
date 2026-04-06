class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        """
        Time:  O(n)
        Space: O(1)

        Key insight: once [L..R] is valid (product < k),
        every subarray ending at R and starting from L..R is valid.
        That's exactly (R - L + 1) new subarrays.

        Edge cases:
        - k <= 1: no subarray can have product < 1 (all nums >= 1)
          → return 0 immediately
        - Single element < k: count 1
        - All elements = 1, k = 2: every subarray is valid
        """
        if k <= 1:
            return 0

        L = 0
        product = 1
        count = 0

        for R in range(len(nums)):
            product *= nums[R]              # expand

            while product >= k:            # invalid → shrink
                product //= nums[L]
                L += 1

            count += R - L + 1             # all subarrays ending at R

        return count