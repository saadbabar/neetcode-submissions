class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            cur = [i, height]
            last_i = i
            while stack and cur[1] <= stack[-1][1]:
                width = i - stack[-1][0]
                area = width * stack[-1][1]
                maxArea = max(maxArea, area)
                last_i = stack[-1][0]
                cur = [last_i, height]
                stack.pop()
            stack.append(cur)
        print(stack)

        cur_i = len(heights)
        while stack:
            cur = stack.pop()
            width = cur_i - cur[0]
            area = width * cur[1]
            maxArea = max(maxArea, area)
        
        return maxArea
            

