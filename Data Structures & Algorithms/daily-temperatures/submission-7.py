class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        nge = []


        response = [0]*len(temperatures)



        for index in range(len(temperatures)-1,-1,-1):


            while nge and nge[-1][0]<=temperatures[index]:

                nge.pop()

            if nge:
                response[index]= nge[-1][1]-index
            
            nge.append((temperatures[index],index))
        


        return response
            



        