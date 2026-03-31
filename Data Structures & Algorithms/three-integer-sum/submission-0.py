from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        response = []

        for i in range(len(nums)):
            # Step 2: Skip duplicate elements
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            j, k = i + 1, len(nums) - 1

            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum > target:
                    k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    response.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for the second and third numbers
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return response