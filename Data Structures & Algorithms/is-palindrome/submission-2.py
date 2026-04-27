class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(char.lower() for char in s if char.isalnum())
        s = 0
        e = len(string) - 1

        while s <= e:
            if string[s] != string[e]:
                return False
            s +=1
            e -=1
        return True
                
                