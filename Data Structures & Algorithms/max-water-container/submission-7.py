class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        max_area = 0

        def _update_max_area(L, R):
            nonlocal max_area
            h = min(heights[L], heights[R])
            area = h * (R - L)
            max_area = max(max_area, area)

        while left < right:
            _update_max_area(left, right)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area