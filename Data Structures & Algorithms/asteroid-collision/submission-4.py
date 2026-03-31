# ------------------------------------------------------
# ✅ Problem: Asteroid Collision
#    (LeetCode 735: https://leetcode.com/problems/asteroid-collision/)
# ------------------------------------------------------
# Given a list of integers representing asteroids in a row:
# - Positive: moving right, Negative: moving left.
# - When two asteroids meet, the smaller one explodes.
# - If same size, both explode.
# - Asteroids moving in the same direction never meet.

# Return the state of asteroids after all collisions.
# # 
# Example:
#   Input:  [5, 10, -5]
#   Output: [5, 10]

#   Input:  [8, -8]
#   Output: []

#   Input:  [10, 2, -5]
#   Output: [10]
# ------------------------------------------------------

# 1. Explore:
#    - Input: asteroids (List[int]), + right, - left
#    - Output: List[int], survivors in order

# 2. Brainstorm:
#    - Use a stack to keep "right-moving" asteroids.
#    - When a new left-moving asteroid appears:
#        - While stack top is right-moving and hasn't "exploded," resolve collision:
#            * If curr is larger, pop stack & continue.
#            * If curr is equal, pop stack and discard curr.
#            * If stack top is larger, discard curr.
#    - After all collisions, stack holds survivors.

# 3. Plan:
#    - For each asteroid:
#        - If right-moving, push to stack.
#        - If left-moving:
#           While stack is nonempty and top is right-moving and abs(curr) >= top:
#               - If abs(curr) > top: pop and continue loop
#               - If abs(curr) == top: pop and discard curr (break loop)
#               - If abs(curr) < top: discard curr (break loop)
#           If curr did not explode, push curr to stack.

# 4. Implement:
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for val in asteroids:
            while stack and val < 0 < stack[-1]:
                # Collision occurs: right-moving top and left-moving val
                if abs(val) > stack[-1]:
                    stack.pop()
                    continue           # Current asteroid keeps moving
                elif abs(val) == stack[-1]:
                    stack.pop()        # Both explode
                    break              # Current asteroid is gone
                else:
                    break              # Current asteroid explodes
            else:
                # No collision, push asteroid
                if not stack or val > 0 or stack[-1] < 0:
                    stack.append(val)
                elif val < 0 and not stack:
                    stack.append(val)
        return stack

# 6. Edge Cases:
#    - All right-moving: [1, 2, 3] => [1, 2, 3]
#    - All left-moving: [-1, -2, -3] => [-1, -2, -3]
#    - Large vs. small: [1, -2] => [-2]

# 7. Complexity:
#    - Time: O(n), each asteroid enters and leaves stack at most once.
#    - Space: O(n), for stack.

# ------------------------------------------------------
# Pattern Recap:
#     - Monotonic Stack sub-pattern for resolving collisions in a stream.
#     - Stack holds possible "survivors" (right movers).
#     - Chain-collisions handled with while/continue.
# ------------------------------------------------------
