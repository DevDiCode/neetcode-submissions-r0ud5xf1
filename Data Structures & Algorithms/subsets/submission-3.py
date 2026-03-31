class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        response = []

        def helper(index,curr):


            response.append(curr.copy())

            for i in range(index,len(nums)):

                if i>index and nums[i]==nums[i-1]:
                    continue
                

                curr.append(nums[i])
                helper(i+1,curr)
                curr.pop()
        
        helper(0,[])
        return response


        
