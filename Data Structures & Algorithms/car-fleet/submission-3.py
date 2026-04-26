class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:



        cars = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append((p, time))

        # 2) Sort by position ascending (smallest position first)
        cars.sort(reverse=True)  # pattern: sort one way, traverse from the opposite side

        # 3) Reverse traversal from the car closest to the target
        fleets = 0
        slowest_time = 0.0  # latest (slowest) arrival time of fleets in front


        stack = []
        for pos, time in cars:

            
            if not stack or time>stack[-1]:
                stack.append(time)
            
            else:
                pass
            
        
        return len(stack)
            





