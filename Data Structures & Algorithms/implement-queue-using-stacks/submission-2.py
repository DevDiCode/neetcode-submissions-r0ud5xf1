# -------------------------------------------
# ✅ PROBLEM: Implement Queue using Stacks
# 💡 PATTERN: Stack/Queue Simulation
# 🎯 GOAL: Simulate FIFO queue using only LIFO stacks
# -------------------------------------------

# 1. Explore:
#    - Operations: push(x), pop(), peek(), empty()
#    - Must use two stacks (no native queue)
#    - Input: integers via push; Output: return front for pop/peek; True/False on empty

# 2. Brainstorm:
#    - Use two stacks: in_stack (for push), out_stack (for pop/peek)
#    - To dequeue/peek: If out_stack empty, move all elements from in_stack → out_stack (reverses order)
#    - Pop/peek from out_stack

# 3. Plan:
#    - push(x): in_stack.append(x)
#    - pop(): If out_stack empty, transfer all from in_stack to out_stack, then out_stack.pop()
#    - peek(): As above, but return out_stack[-1]
#    - empty(): True if both stacks empty

# 4. Implement:

class MyQueue:

    def __init__(self):
        # Stack for enqueue
        self.s1 = []
        # Stack for dequeue
        self.s2 = []

    def push(self, x: int) -> None:
        # Always push to s1
        self.s1.append(x)

    def pop(self) -> int:
        # Pour elements if needed, then pop from s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        # Pour elements if needed, then peek from s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks empty
        return not self.s1 and not self.s2

# 5. Verify (sample driver code):

q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())   # Output: 1
print(q.pop())    # Output: 1
print(q.empty())  # Output: False

# 6. Edge Cases:
#    - What if pop/peek on empty? (Error as with any empty stack, can customize)
#    - Multiple pushes before pops: Still FIFO

# 7. Complexity:
#    - Time: push O(1), pop/peek amortized O(1)
#    - Space: O(n) total for both stacks

# -------------------------------------------
# Pattern Recap: Two stacked used to reverse input order to output queue in FIFO fashion
# -------------------------------------------
