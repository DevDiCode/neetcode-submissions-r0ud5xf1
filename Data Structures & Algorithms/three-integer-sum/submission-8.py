class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        nums.sort()
        response = []

        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue
            

            target = -nums[i]

            left = i+1
            right = len(nums)-1

            while left < right:
                
                curr_sum = nums[left]+nums[right]

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                
                else :

                    response.append([nums[i],nums[left],nums[right]])


                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    

                    left+=1
                    right-=1
            
        return response




