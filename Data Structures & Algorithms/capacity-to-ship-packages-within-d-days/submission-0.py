class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def is_condition(capacity):

            max_days=1

            total_wt = 0 

            for val in weights:
                if val+total_wt<=capacity:
                    total_wt+=val
                
                else:
                    total_wt = val
                    max_days+=1
                    
            return max_days<=days
        

        L = max(weights)
        R = sum(weights)

        while L<R:
            mid = (L+R)//2


            if is_condition(mid):
                R = mid
            
            else:
                L = mid+1
        
        return L

        