class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        prefix_list = [1] * len(nums)
        for i in range(len(nums)):
            prefix_list[i] = prefix
            prefix *= nums[i]
        postfix = 1
        postfix_list = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            postfix_list[i] = postfix
            postfix *= nums[i]
        for i in range(len(nums)):
            output.append(prefix_list[i] * postfix_list[i])

        return output