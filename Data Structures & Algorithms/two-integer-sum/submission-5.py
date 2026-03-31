"""

Explore


input : list o fnumerbs
output: Integer 

BrainStorm: 
-> can every number with every otehr numbeer - 

-> use a hashmap

Approach:
-> Iterate evey number 
    -> check if the differnece is in lookup 
        -> if present return anser with index position 
    
    -> add numbers iwth their idexes

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        if not nums:
            return [-1,-1]

        lookup = {}

        for index, val in enumerate(nums):

            diff = target-val

            if diff in lookup:
                return [lookup[diff],index]
            
            lookup[val] = index
        


        