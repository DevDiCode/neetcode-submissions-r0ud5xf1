class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        response = [0]*len(temperatures)
        stack  = []
        

        for index in range(len(temperatures)-1,-1,-1):
            
            val = temperatures[index]
            while stack and stack[-1][0]<=val:
                stack.pop()

            if stack:
                response[index] = stack[-1][1] - index


            stack.append((val,index))
        
        return response
        