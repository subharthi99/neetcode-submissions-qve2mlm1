class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # words = len(strs)
        # l = min([len(word) for word in strs])
        # for i in range(0, l):
        if len(strs) == 0: return ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return word[:i]
        return strs[0]