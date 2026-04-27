class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in my_dict:
                if not stack or stack.pop() != my_dict[char]:
                    return False
            else:
                stack.append(char)
        return not stack
