class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True
        


        lookup = {"}":"{", "]":"[",")":"("}


        stack = []


        for val in s:
            if val in lookup:

                if stack and stack[-1]==lookup[val]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(val)
        
        return True if not stack else False