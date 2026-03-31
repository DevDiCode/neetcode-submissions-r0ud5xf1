class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        response = []



        def helper(index, curr, csum):
            
            if csum>target:
                return 

            if csum ==target:
                response.append(curr.copy())
                return 

        

            for i in range(index,len(nums)):


                curr.append(nums[i])
                helper(i,curr,csum+nums[i])
                curr.pop()


        helper(0,[],0)
        return response