class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        combinations = []
        for i in range(len(speed)):
            combinations.append((position[i], speed[i]))
        combinations.sort(key= lambda x: x[0], reverse = True)

        for pos, spd in combinations:
            dist = ((target - pos) / spd)
            while not stack or dist > stack[-1]:
                stack.append(dist)
        return len(stack)
        
        