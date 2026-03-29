class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        un_set = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 in un_set:
                continue
            curr_len = 1
            while nums[i] + 1 in un_set:
                curr_len += 1
                nums[i] += 1
            res = max(res, curr_len)
        return res
            