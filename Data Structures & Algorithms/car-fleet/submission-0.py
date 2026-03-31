class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Combine position and speed, and sort cars by position in descending order
        pair = sorted(zip(position, speed), reverse=True)
        
        stack = []  # Stack to store the time to reach the target for each fleet
        
        for p, s in pair:
            # Calculate time to reach the target for the current car
            time = (target - p) / s
            
            # Check if the current car forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
