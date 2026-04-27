class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for string in strs:
            new_string += str(len(string)) + '#' + string
        return new_string
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0 
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
            
