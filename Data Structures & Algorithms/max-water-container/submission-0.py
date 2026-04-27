class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        cur_h = 0
        max_h = 0
        while (start < end):
            cur_h = min(heights[start], heights[end]) * (end - start)
            max_h = max(cur_h, max_h)
            if (heights[start] > heights[end]):
                end -=1
            else:
                start +=1
        return max_h