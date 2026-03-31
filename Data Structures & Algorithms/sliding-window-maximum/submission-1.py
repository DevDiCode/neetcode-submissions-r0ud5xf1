class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices, not values
        res = []
        L = 0

        for R in range(len(nums)):
            # Remove all smaller elements from back
            while q and nums[q[-1]] < nums[R]:
                q.pop()

            q.append(R)

            # Remove leftmost if it’s outside the current window
            if q[0] < L:
                q.popleft()

            # Only append to result when window is of size k
            if R - L + 1 == k:
                res.append(nums[q[0]])
                L += 1

        return res