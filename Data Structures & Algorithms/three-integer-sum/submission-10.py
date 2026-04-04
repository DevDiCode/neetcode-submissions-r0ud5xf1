class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        if not nums:
            return []
        


        nums.sort()

        response = []
        

        for index, val in enumerate(nums):

            if index>0 and nums[index]==nums[index-1]:
                continue
            
            left = index + 1  # Step 2: Initialize left pointer
            right = len(nums) - 1  # Step 3: Initialize right pointer

            while left < right:
                csum = val + nums[left] + nums[right]

                if csum>0:
                    right-=1
                
                elif csum<0:
                    left+=1
                
                else:

                    response.append([nums[index], nums[left],nums[right]])


                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

        return response
