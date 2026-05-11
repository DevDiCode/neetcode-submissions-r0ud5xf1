class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:


        self.total=0 

        def helper(index,csum):


            self.total+=csum



            for i in range(index,len(nums)):

                value = nums[i]

                helper(i+1,csum^value)
        

        helper(0,0)
        return self.total
        