class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res: List[List[int]] = []
        path: List[int] = []
        n = len(nums)

        nums.sort()

        def helper(i: int) -> None:
            if i == n:
                res.append(path.copy())
                return

            # 1) Pick nums[i]
            path.append(nums[i])
            helper(i + 1)
            path.pop()

            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1

            # 2) Not-pick nums[i]
            helper(i + 1)

        helper(0)
        return res

        