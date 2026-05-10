class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        response = []
        
        lookup = set()

        nums.sort()

        def helper(index,curr):

            if len(curr)==len(nums):
                response.append(curr.copy())
                return 
            

            for i in range(len(nums)):

                if i in lookup:
                    continue

                
                if i>0 and nums[i]==nums[i-1] and (i-1) not in lookup:
                    continue

                
                lookup.add(i)
                curr.append(nums[i])
                helper(i+1, curr)
                lookup.remove(i)
                curr.pop()
        

        helper(0,[])
        return response
