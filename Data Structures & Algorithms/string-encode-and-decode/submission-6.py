  
class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_str = []
        for word in strs:
            encoded_str.append(str(len(word)))
            encoded_str.append('#')
            encoded_str.append(word)
        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sol = []
        count = 0
        while count < len(s):
            # Find the length of the next word
            j = count
            while s[j] != '#':
                j += 1
            length = int(s[count:j])
            # Extract the word
            word = s[j+1:j+1+length]
            sol.append(word)
            # Move to the next word
            count = j + 1 + length
        return sol