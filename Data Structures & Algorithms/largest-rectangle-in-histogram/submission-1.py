class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Function to calculate Next Smaller Element indices
        def nse(arr):
            res = [n] * n  # Initialize with n (beyond the last index)
            stack = []
            for i in range(len(arr) - 1, -1, -1):
                while stack and stack[-1][0] >= arr[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1][1]
                stack.append((arr[i], i))
            return res

        # Function to calculate Previous Smaller Element indices
        def pse(arr):
            res = [-1] * n  # Initialize with -1 (before the first index)
            stack = []
            for index, val in enumerate(arr):
                while stack and stack[-1][0] >= val:
                    stack.pop()
                if stack:
                    res[index] = stack[-1][1]
                stack.append((val, index))
            return res

        # Calculate NSE and PSE
        array_nse = nse(heights)
        array_pse = pse(heights)

        # Calculate maximum rectangle area
        max_area = 0
        for i in range(n):
            width = array_nse[i] - array_pse[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area
