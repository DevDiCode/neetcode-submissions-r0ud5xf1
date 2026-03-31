# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         self.count = 0

#         def helper(index, csum):
#             if index < 0:
#                 if csum == target:
#                     self.count += 1
#                 return

#             # Choose +
#             helper(index-1, csum + nums[index])

#             # Choose -
#             helper(index-1, csum - nums[index])

#         helper(len(nums)-1, 0)
#         return self.count
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def helper(index, csum):
            if index < 0:
                return 1 if csum == target else 0

            if (index, csum) in dp:
                return dp[(index, csum)]

            # Choice: add nums[index]
            add = helper(index-1, csum + nums[index])

            # Choice: subtract nums[index]
            subtract = helper(index-1, csum - nums[index])

            dp[(index, csum)] = add + subtract
            return dp[(index, csum)]

        return helper(n-1, 0)
