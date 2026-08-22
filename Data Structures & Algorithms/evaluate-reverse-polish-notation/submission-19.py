class Solution:
    def evaluate_expression(self, digit1: int, digit2: int, operation: str):
        if operation == "+":
            return digit2 + digit1
        if operation == "-":
            return digit2 - digit1
        if operation == "*":
            print(digit1)
            print(digit2)
            return digit2 * digit1
        if operation == "/":
            return int(digit2/digit1)

    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                digit1 = stack.pop()
                digit2 = stack.pop()
                res = self.evaluate_expression(digit1, digit2, token)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1] if len(stack) == 1 else 0