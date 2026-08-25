class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Keep a stack for the time
        stack = []
        pairs = [[] for _ in range(len(position))]

        for i in range(len(position)):
            pairs[i] = [position[i], speed[i]]
        
        pairs.sort(key=lambda x: x[0], reverse=True)

        for position, speed in pairs:
            time = (target - position) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)