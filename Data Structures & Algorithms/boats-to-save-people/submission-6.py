class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boats = 0 

        L = 0 
        R = len(people)-1
        people.sort()

        while L<=R:

            if people[L]+people[R]<=limit:
                L+=1
            

            R-=1
            boats+=1
        
        return boats
        