class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0

        water = 0
        n = len(height)

        # Step 1: Calculate left max for each index
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Step 2: Calculate right max for each index
        right_max = [0] * n
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Step 3: Calculate trapped water
        for i in range(n):
            trapped = min(left_max[i], right_max[i]) - height[i]
            if trapped > 0:
                water += trapped

        return water
