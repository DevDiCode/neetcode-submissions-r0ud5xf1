class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        L = 0 
        R = len(people)-1

        people.sort()
        count = 0 

        while L<=R:


            if L==R:
                L+=1
            

            if people[L] + people[R]<=limit:
                L+=1
                R-=1
            
            else:
                R -= 1

            count += 1

        return count


