class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        cur_max = ''

        for i in range(len(s) + 1):
            cur_string = ''
            for j in range(i):
                cur_string = s[j:i]
                if (cur_string == cur_string[::-1]) and (len(cur_string) > len(cur_max)):
                    cur_max = cur_string

        return cur_max