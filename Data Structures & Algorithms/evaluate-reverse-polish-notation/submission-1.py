from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for val in tokens:

            if val in "*/-+":
                b = res.pop()
                a = res.pop()
                if val == "+":

                    res.append(a + b)
                elif val == "-":
                
                    res.append(a - b)
                elif val == "*":
                    
                    res.append(a * b)
                elif val == "/":
                    res.append(int(a / b))  # truncate toward zero
            else:
                res.append(int(val))

        return res[-1]
