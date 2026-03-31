class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        response = []

        def helper(index,curr):


            if len(curr)==k:
                response.append(curr.copy())
                return 

            if index>n:
                return 
            

            curr.append(index)
            helper(index+1,curr)
            curr.pop()
            helper(index+1,curr)
        
        helper(1,[])
        return response 
        