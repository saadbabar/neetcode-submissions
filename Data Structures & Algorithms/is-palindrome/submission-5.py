class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        for char in s:
            if char.isalnum():
                cleaned_string += char
        
        # 2 pointers
        a, b = 0, len(cleaned_string) - 1

        while a < b:
            if cleaned_string[a].lower() == cleaned_string[b].lower():
                a += 1
                b -= 1
            else:
                return False

        return True