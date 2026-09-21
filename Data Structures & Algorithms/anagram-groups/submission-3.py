class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idx_map = defaultdict(list)

        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            idx_map[tuple(freq)].append(word)
        return list(idx_map.values())