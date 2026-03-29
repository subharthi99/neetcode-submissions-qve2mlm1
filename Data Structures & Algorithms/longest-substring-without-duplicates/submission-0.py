class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        currset = set()
        for r in range(len(s)):
            while s[r] in currset:
                currset.remove(s[l])
                l += 1
            currset.add(s[r])
            res = max(res, r - l + 1)
        return res 