class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        max_len = 0
        for i in range(len(s)):
            j = i
            while True:
                if(s[j] in my_set):
                    max_len = max(max_len, len(my_set))
                    my_set.clear()
                    break
                else:
                    my_set.add(s[j])
                    if j < len(s) - 1:
                        j+=1
        return max_len

