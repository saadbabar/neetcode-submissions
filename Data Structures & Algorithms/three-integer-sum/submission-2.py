class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        sol = set()
        ans = list()
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                if (s[i] + s[j] + s[k] == 0):
                    sol.add((s[i], s[j], s[k]))
                    j += 1
                    k -= 1
                elif (s[i] + s[j] + s[k] < 0):
                    j +=1
                else:
                    k -= 1
        return [list(triplet) for triplet in sol]
                