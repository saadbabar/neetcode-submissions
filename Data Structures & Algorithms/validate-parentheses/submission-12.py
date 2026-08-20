class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                continue
            if char in mappings.keys():
                if stack and mappings[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
            