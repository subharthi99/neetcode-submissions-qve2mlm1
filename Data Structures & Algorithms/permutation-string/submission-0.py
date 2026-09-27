class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1): return False
        
        s1count, s2count = {}, {}
        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i], 0)
            s2count[s2[i]] = 1 + s2count.get(s2[i], 0)
        if s1count == s2count: return True
        l = len(s1)
        for r in range(len(s1), len(s2)):
            
            s2count[s2[r]] = 1 + s2count.get(s2[r], 0)
            s2count[s2[r - l]] -= 1
            if s2count[s2[r - l]] == 0: del s2count[s2[r - l]]
            if s1count == s2count: return True

        return False