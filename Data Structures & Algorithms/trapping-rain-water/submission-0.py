class Solution:
    def trap(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        # Step 1: Calculate left max for each index
        left_max = float("-inf")
        left_array = []
        for val in height:
            left_max = max(val, left_max)
            left_array.append(left_max)

        # Step 2: Calculate right max for each index (traverse from right to left)
        right_max = float("-inf")
        right_array = []
        for val in reversed(height):
            right_max = max(val, right_max)
            right_array.append(right_max)
        right_array.reverse()  # reverse to align with `height` indices

        # Step 3: Calculate water trapped
        water = 0
        for i, val in enumerate(height):
            trapped = min(left_array[i], right_array[i]) - val
            if trapped > 0:
                water += trapped

        return water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        # Step 1: Calculate left max for each index
        left_max = float("-inf")
        left_array = []
        for val in height:
            left_max = max(val, left_max)
            left_array.append(left_max)

        # Step 2: Calculate right max for each index (traverse from right to left)
        right_max = float("-inf")
        right_array = []
        for val in reversed(height):
            right_max = max(val, right_max)
            right_array.append(right_max)
        right_array.reverse()  # reverse to align with `height` indices

        # Step 3: Calculate water trapped
        water = 0
        for i, val in enumerate(height):
            trapped = min(left_array[i], right_array[i]) - val
            if trapped > 0:
                water += trapped

        return water
