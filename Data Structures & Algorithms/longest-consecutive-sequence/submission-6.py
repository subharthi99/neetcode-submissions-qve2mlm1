class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_l, i = 0, 0
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_l = 1
                while num + 1 in nums_set:
                    curr_l += 1
                    num += 1
                max_l = max(max_l, curr_l)
            i += 1
        return max_l