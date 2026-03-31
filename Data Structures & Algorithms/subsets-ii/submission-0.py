class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        response = []
        nums.sort()

        def helper(ind, curr):

            response.append(curr.copy())

            for i in range(ind, len(nums)):

                if i!=ind and nums[i]==nums[i-1]:
                    continue

                curr.append(nums[i])
                helper(i+1,curr)
                curr.pop()



        helper(0,[])

        return response