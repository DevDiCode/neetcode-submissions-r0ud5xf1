# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         for i in range(len(nums)):

#             total = 0 

#             for j in range(i,len(nums)):

#                 total+=nums[j]

#                 if total==k:
#                     count+=1
        
#         return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        lookup = {0:1}
        prefix_sum = 0
        count = 0 
        for num in nums:
            prefix_sum+=num

            diff = prefix_sum-k

            count+= lookup.get(diff,0)

            lookup[prefix_sum] = lookup.get(prefix_sum,0)+1
        
        return count
