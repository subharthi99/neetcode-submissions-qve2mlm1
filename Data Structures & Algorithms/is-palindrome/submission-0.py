class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_s = ""
        for c in s:
            if c.isalnum():
                clean_s += c.lower()
        print(clean_s)
        l, r = 0, len(clean_s) - 1
        
        while l <= r:
            print(clean_s[r])
            if clean_s[l] != clean_s[r]:
                print(clean_s[l], clean_s[r])
                return False
            l += 1
            r -= 1
        return True