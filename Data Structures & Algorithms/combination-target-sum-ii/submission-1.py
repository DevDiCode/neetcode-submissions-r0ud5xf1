class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        response = []

        candidates.sort()



        def helper(index,curr,csum):


            if csum==target:
                response.append(curr.copy())
                return 
            
            if csum>target:
                return 
        

            for i in range(index,len(candidates)):


                if i>index and candidates[i]==candidates[i-1]:
                    continue
                


                curr.append(candidates[i])
                helper(i+1,curr,csum+candidates[i])
                curr.pop()


        helper(0,[],0)
        return response        