class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        left_max, r_max = height[left], height[right]
        while left < right:
            minimum = min(left_max, r_max)
            if height[left] <= height[right]:
                left+=1
                if height[left] > left_max:
                    left_max = height[left]
                if (height[left] < minimum):
                    res += minimum - height[left]
            else:
                right -=1
                if height[right] > r_max:
                    r_max = height[right]
                if (height[right] < minimum):
                    res += minimum - height[right]
        return res


            
