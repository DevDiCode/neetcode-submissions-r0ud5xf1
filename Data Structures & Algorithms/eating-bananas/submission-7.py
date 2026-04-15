class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        L = 1
        R = max(piles)



        def is_condition(num):

            total_hours = 0 


            for val in piles:

                if val>mid:
                    total_hours+= math.ceil(val/mid)
                else:
                    total_hours+=1
            

            return total_hours<=h


    





        while L<R:

            mid = (L+R)//2

            if is_condition(mid):
                R = mid
            
            else:
                L = mid+1
        
    
        return L 


        
