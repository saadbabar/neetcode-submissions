class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        away = 0
        res = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = away
                    break
                else:
                    away +=1
            away = 0
        return res




