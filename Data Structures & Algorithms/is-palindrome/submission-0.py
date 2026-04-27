class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        for letter in s:
            if (letter.isalpha() or letter.isdigit()):
                list1.append(letter.lower())
        p1 = 0
        p2 = len(list1) - 1
        while (p1 <= p2):
            if (list1[p1] != list1[p2]):
                return False
            p1+=1
            p2-=1
        return True