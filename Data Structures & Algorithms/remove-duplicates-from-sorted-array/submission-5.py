class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        L = 0 

        for R in range(1,len(nums)):

            if nums[R]!=nums[L]:
                L+=1
                nums[L]=nums[R]
        return L+1
            
            


        