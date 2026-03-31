class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        response = []

        lookup = set()
        def helper(curr):

            if len(curr)==len(nums):
                response.append(curr.copy())
                return 

            

            for i in range(len(nums)):


                if i in lookup:
                    continue
                
                lookup.add(i)
                curr.append(nums[i])
                helper(curr)
                curr.pop()
                lookup.remove(i)

        helper([])
        return response
        