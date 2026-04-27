class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for char in s:
            if char in my_map.keys():
                if not stack or my_map[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        return True if not stack else False