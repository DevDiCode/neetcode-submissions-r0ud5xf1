from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for val in tokens:
            if val == "+":
                b = res.pop()
                a = res.pop()
                res.append(a + b)
            elif val == "-":
                b = res.pop()
                a = res.pop()
                res.append(a - b)
            elif val == "*":
                b = res.pop()
                a = res.pop()
                res.append(a * b)
            elif val == "/":
                b = res.pop()
                a = res.pop()
                res.append(int(a / b))  # truncate toward zero
            else:
                res.append(int(val))

        return res[-1]
