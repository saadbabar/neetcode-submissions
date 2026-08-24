class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        if not temperatures:
            return []

        for i, temp in enumerate(temperatures):
            cur = (temp, i)
            while stack and cur[0] > stack[-1][0]:
                num = stack.pop()
                res[num[1]] = cur[1] - num[1]
                print(num[1])

            stack.append(cur)
        return res