class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            my_dict[key].append(word)
        return list(my_dict.values())