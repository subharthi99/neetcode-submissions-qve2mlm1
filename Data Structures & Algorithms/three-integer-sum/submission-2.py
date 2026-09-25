class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            print("value of i1:", i)
            if nums[i] == nums[i - 1] and i > 0:
                print("value of i2:", i)
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res