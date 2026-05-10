class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        response = []
        
        lookup = set()

        def helper(index,curr):

            if len(curr)==len(nums):
                response.append(curr.copy())
                return 
            

            for i in range(len(nums)):

                if i in lookup:
                    continue
                
                lookup.add(i)
                curr.append(nums[i])
                helper(i+1, curr)
                lookup.remove(i)
                curr.pop()
        

        helper(0,[])
        return response




