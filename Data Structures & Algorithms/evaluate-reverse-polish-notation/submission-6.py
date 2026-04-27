class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: 
            return int(tokens[-1])
        stk = []
        for char in tokens:
            if char.lstrip('-').isdigit():
                stk.append(char)
            else:
                val1 = int(stk.pop())
                val2 = int(stk.pop())
                if char == "+": stk.append(val1 + val2)
                elif char == "-": stk.append(val2 - val1)
                elif char == "*": stk.append(val1 * val2)
                else: stk.append(int(val2/val1))
        return stk[-1]                