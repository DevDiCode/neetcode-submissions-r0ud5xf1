"""
Explore:
->  input : array
    output : True/ False

Assumption:
-> The input can be empty : yes
-> Theer may no be repead values

Brainstorm : 

1 -> Compare value iwth every other value -> O (N)2
2. -> use a hash map to check if the value if alsrady resent 


"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        if not nums:
            return False

        
        lookup = set()

        for val in nums:
            if val in lookup:
                return True
            
            lookup.add(val)
        
        return False

        