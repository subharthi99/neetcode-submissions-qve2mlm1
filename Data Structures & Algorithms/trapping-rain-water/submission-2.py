class Solution:
    def trap(self, height: List[int]) -> int:
        # # maintain three arrays - maxL, maxR array
        # # min(maxL[i], maxR[i]) - height[i] > 0 then add
        # maxL, maxR = [0] * len(height), [0]*len(height)
        # tot = 0

        # i = 0
        # currMax = 0
        # while i < len(height):
        #     curr = height[i] 
        #     maxL[i] = currMax
        #     currMax = max(currMax, curr)
        #     i += 1
        
        # i = len(height) - 1
        # currMax = 0
        # while i >= 0:
        #     curr = height[i]
        #     maxR[i] = currMax
        #     currMax = max(currMax, height[i])
        #     i -= 1
        
        # for i in range(len(height)):
        #     val = min(maxL[i], maxR[i]) - height[i]
        #     tot += val if val > 0 else 0

        # return tot
        l, r = 0, len(height) - 1
        res = 0
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res



