from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for letter in s:
            map1[letter] += 1
        
        for letter in t:
            map2[letter] += 1

        return True if map1 == map2 else False