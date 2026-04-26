class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        stack = []


        for asteroid in asteroids:
            # We will try to resolve collisions only if needed.
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack[-1]
                if abs(top) < abs(asteroid):
                    # Top is smaller: it explodes, keep checking earlier ones.
                    stack.pop()
                    # Keep while loop running to check with new top.
                    continue
                elif abs(top) == abs(asteroid):
                    # Both same size: both explode. Remove top and "discard" asteroid.
                    stack.pop()
                    # Current asteroid is destroyed; skip pushing it.
                    break
                else:
                    # Top is larger: asteroid is destroyed.
                    # Just discard asteroid by breaking without pushing.
                    break
            else:
                # The while loop didn't break:
                #   - either we never entered it (no collision case), or
                #   - we popped smaller tops until stack empty or top is left-moving.
                # In both situations, asteroid survives → push it.
                stack.append(asteroid)

        return stack