class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        res = []

            #123
        def helper(index,curr):
            

            res.append(curr.copy())


            for i in range(index,len(nums)):

                curr.append(nums[i])
                helper(i+1,curr)
                curr.pop()

        helper(0,[])
        return res        