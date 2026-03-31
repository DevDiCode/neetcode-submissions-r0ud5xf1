class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        result = [0]*n

        stack = []


        for i in range(len(temperatures)-1,-1,-1):

            curr_temperature = temperatures[i]

            count = 0
            while stack and stack[-1][0]<=curr_temperature:
                
                stack.pop()
                count+=1
            


            if stack:
                result[i] = stack[-1][1] - i
            
            stack.append([curr_temperature,i])

        return result

            
        