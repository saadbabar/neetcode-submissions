class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1, list2 = sorted(s), sorted(t)
        return list1 == list2
        
    