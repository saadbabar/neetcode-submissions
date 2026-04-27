class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char.lstrip('-').isdigit():
                stack.append(int(char))
            else:
                digit1 = stack.pop()
                digit2 = stack.pop()
                res = 0
                if char == "+":
                    res = digit1 + digit2
                elif char == "-":
                    res = digit2 - digit1
                elif char == "*":
                    res = digit1 * digit2
                else:
                    res = int(digit2/digit1)
                stack.append(res)
        return stack[0]