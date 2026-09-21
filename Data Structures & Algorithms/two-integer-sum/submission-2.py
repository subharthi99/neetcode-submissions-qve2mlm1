class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        computed_val = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in computed_val:
                return [computed_val[diff], i]
            computed_val[n] = i
        return