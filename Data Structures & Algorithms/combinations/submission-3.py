class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        response = []

        lookup = set()

        def helper(index, curr):

            if len(curr)==k:
                response.append(curr.copy())
                return 
            


            for i in range(index,n+1):

                curr.append(i)
                helper(i+1,curr)
                curr.pop()
        
        helper(1,[])
        return response