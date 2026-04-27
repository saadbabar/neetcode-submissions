class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0 
        my_dict = defaultdict(int)
        maxLen = 0

        while r != len(s):
            windowLen = r - l + 1
            my_dict[s[r]] += 1
            if windowLen - max(my_dict.values()) <= k:
                maxLen = max(maxLen, windowLen)
                r += 1
            else:
                while windowLen - max(my_dict.values()) > k:
                    my_dict[s[l]] -= 1
                    l +=1
                    windowLen = r - l + 1
                r+=1

        return maxLen








