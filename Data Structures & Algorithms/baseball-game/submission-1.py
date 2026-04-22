class Solution:
    def calPoints(self, operations: List[str]) -> int:


        stack = []


        if not operations:
            return 0
        


        for index, val in enumerate(operations):

            if val in "+CD":

                if val=="+":
                    
                    a=  stack[-1]
                    b = stack[-2]
                    stack.append(int(a+b))
                
                elif val=="C":
                    stack.pop()
                
                else:
                    current_val = stack[-1]
                    stack.append(2*int(current_val))

            else:
                stack.append(int(val))

        
        return sum(stack) if stack else 0
