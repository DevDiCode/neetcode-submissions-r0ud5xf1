class Solution:
    def isValid(self, s: str) -> bool:

        lookup = { "}":"{","]":"[",")":"("}

        stack = []
        for val in s:

            if val in lookup :
                if stack and stack[-1]==lookup[val]:
                    stack.pop()
            
                else:
                    return False
            else:
                stack.append(val)
        
        return not stack



