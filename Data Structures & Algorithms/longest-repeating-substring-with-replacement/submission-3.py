class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        my_dict = defaultdict(int)
        for r in range(len(s)):
            my_dict[s[r]] += 1

            while (r - l + 1 - max(my_dict.values()) > k):
                my_dict[s[l]]-=1
                l +=1
            max_len = max(max_len, r - l + 1)
        return max_len
                



