class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens:
            return 0

        stack: List[int] = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:  # token == "/"
                    # Truncate toward zero
                    stack.append(int(left / right))
            else:
                stack.append(int(token))

        return stack[-1]



