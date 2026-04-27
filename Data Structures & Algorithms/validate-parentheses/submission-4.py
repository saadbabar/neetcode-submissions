class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for bracket in s:
            if bracket in my_dict:
                if not stack or stack.pop() != my_dict[bracket]:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        return True