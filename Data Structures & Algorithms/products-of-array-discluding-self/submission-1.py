class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        postfix= 1

        response = [None]*len(nums)

        for index,val in enumerate(nums):

            response[index] = prefix
            prefix*=val
        
        index = len(nums)-1
        for  val in nums[::-1]:
            
            response[index]*=postfix
            postfix*=val
            index-=1
        

        return response