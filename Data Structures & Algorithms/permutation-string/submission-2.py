class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check_len = len(s2) - len(s1) + 1

        for i in range(check_len):
            if sorted(s2[i:i + len(s1)]) == sorted(s1):
                return True

        return False