class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = [char.lower() for char in s if char.isalnum()]
        p1, p2 = 0, len(new_str) - 1
        while p1 < p2:
            if new_str[p1] != new_str[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True