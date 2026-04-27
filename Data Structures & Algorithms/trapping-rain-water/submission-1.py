class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        res = 0

        while l < r:
            if height[l] <= height[r]:
                l+=1
                lmax = max(lmax, height[l])
                if height[l] < min(lmax, rmax):
                    res += min(lmax, rmax) - height[l]
            else:
                r-=1
                rmax = max(rmax, height[r])
                if height[r] < min(lmax, rmax):
                    res += min(lmax, rmax) - height[r]
        return res