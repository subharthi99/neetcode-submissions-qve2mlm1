class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_set = set()
        l, r = 0, 0 
        longest = 0
        while r < len(s):
            while s[r] in curr_set:
                curr_set.remove(s[l])
                l += 1
            curr_set.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest