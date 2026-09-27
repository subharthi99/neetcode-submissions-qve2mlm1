class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # if len(s2) < len(s1): return False
        
        # s1count, s2count = {}, {}
        # for i in range(len(s1)):
        #     s1count[s1[i]] = 1 + s1count.get(s1[i], 0)
        #     s2count[s2[i]] = 1 + s2count.get(s2[i], 0)
        # if s1count == s2count: return True
        # l = len(s1)
        # for r in range(len(s1), len(s2)):
        #     s2count[s2[r]] = 1 + s2count.get(s2[r], 0)
        #     s2count[s2[r - l]] -= 1
        #     if s2count[s2[r - l]] == 0: del s2count[s2[r - l]]
        #     if s1count == s2count: return True

        # return False

        if len(s2) < len(s1): return False
        
        s1count = [0] * 26
        s2count = [0] * 26

        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1count[i] == s2count[i] else 0
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            curri = ord(s2[r]) - ord('a')
            s2count[curri] += 1
            if s1count[curri] == s2count[curri]:
                matches += 1
            elif s1count[curri] + 1 == s2count[curri]:
                matches -= 1
            
            curri = ord(s2[l]) - ord('a')
            s2count[curri] -= 1
            if s1count[curri] == s2count[curri]:
                matches += 1
            elif s1count[curri] - 1 == s2count[curri]:
                matches -= 1
            l += 1
        return matches == 26