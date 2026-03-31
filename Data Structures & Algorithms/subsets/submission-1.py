class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        response = []



        def helper(index, curr):

            if index>=len(nums):
                response.append(curr.copy())
                return

            curr.append(nums[index])
            helper(index+1,curr)
            curr.pop()
            helper(index+1,curr)

        helper(0,[])
        return response

        
        
