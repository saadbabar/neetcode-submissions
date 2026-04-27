class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for word in strs:
            new_string += word + "\t"
        return new_string

    def decode(self, s: str) -> List[str]:
        line = s.split("\t")
        return line[0:len(line) - 1]
