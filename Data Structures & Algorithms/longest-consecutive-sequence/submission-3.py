class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_l, i = 0, 0
        while i < len(nums):
            if nums[i] - 1 not in nums_set:
                current_num, curr_l = nums[i], 1
                while current_num + 1 in nums_set:
                    curr_l += 1
                    current_num += 1
                max_l = max(max_l, curr_l)
            i += 1
        return max_l