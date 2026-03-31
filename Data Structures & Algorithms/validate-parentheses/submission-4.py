# ------------------------------------------------------
# ✅ Problem: Valid Parentheses
#         (LeetCode 20: https://leetcode.com/problems/valid-parentheses/)
# ------------------------------------------------------
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
#   Input: s = "()"
#   Output: true
#
# Example 2:
#   Input: s = "()[]{}"
#   Output: true
#
# Example 3:
#   Input: s = "(]"
#   Output: false
# ------------------------------------------------------

# 1. Explore:
#    - Input: string s (only '(', ')', '{', '}', '[', ']')
#    - Output: True if valid, else False
#    - Constraints: Properly matched and nested pairs. Empty string is valid.

# 2. Brainstorm:
#    - Use a stack to keep track of opens.
#    - For closers, check if top of stack matches correct opener.
#    - Use a dict for mapping close to open for constant-time lookups.

# 3. Plan:
#    - Return False for odd-length strings.
#    - Walk string, push opens to stack.
#    - For closes: match top of stack, else return False.
#    - At end: stack must be empty.

# 4. Implement:
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False  # Odd lengths can never be matched
        
        # Maps closing bracket to its respective opening bracket
        hashmap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in hashmap:  # If this is a closing bracket
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()  # Found a matching open, remove it
                else:
                    return False # Mismatch or stack empty; invalid
            else:
                stack.append(char)  # It's an opening bracket, push to stack

        return not stack  # Valid iff every opener has been matched

# 5. Verify:
sol = Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([)]"))      # False
print(sol.isValid("{[]}"))      # True
print(sol.isValid(""))          # True

# 6. Edge Cases:
#    - ""         => True (empty: valid)
#    - "(("       => False (unmatched opener)
#    - "))"       => False (unmatched closer)
#    - "{[)]}"    => False (wrongly nested)
#    - "()"       => True

# 7. Complexity:
#    - Time: O(n) (one scan, each char processed once)
#    - Space: O(n) (worst case: all opens in stack)

# ------------------------------------------------------
# Pattern Recap:
#   - Stack for matching open/close.
#   - Dict for close→open mapping.
#   - Valid iff stack is empty at end.
# ------------------------------------------------------
