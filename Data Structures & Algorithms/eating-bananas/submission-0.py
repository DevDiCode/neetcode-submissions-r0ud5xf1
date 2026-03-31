class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        res = 0


        def isCondition(rate):

            time = 0 


            for pile in piles:

                if pile<rate:
                    time+=1
                
                else:
                    count = math.ceil(pile/rate)
                    time+=count
            

            return time<=h


        while L<R:
            mid = (L+R)//2

            if isCondition(mid):
                R = mid
            
            else:
                L = mid+1
        


        return L