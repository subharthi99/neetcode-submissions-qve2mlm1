class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for c in s:
            if c.isalnum():
                clean_str += c.lower()

        l, r = 0, len(clean_str) - 1
        while l <= r:
            if clean_str[l] != clean_str[r]:
                return False
            l += 1
            r -= 1
        return True
