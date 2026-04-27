class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        count = 0

        for i in range(len(s) + 1):
            cur = ''
            for j in range(i):
                cur = s[j:i]
                if(cur == cur[::-1]):
                    count +=1

        return count
