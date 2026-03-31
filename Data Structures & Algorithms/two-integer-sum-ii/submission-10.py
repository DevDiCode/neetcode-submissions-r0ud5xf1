class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        response = []


        i = 0 
        j = len(numbers)-1


        while i<j:
            curr_sum = numbers[i]+numbers[j]

            if curr_sum>target:
                j-=1
            
            elif curr_sum<target:
                i+=1
            
            else:
                if numbers[i]!=numbers[j]:
                    return [i+1,j+1]
                
                else:
                    i+=1
                