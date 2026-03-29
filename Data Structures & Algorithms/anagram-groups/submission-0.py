class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## keys = countmaps or freq_map list
        ## vals = [list of original vals] 
        ## for loops (nested) - main for each string 
            ## and one more to count thru the string by each char
        main_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            main_map[tuple(count)].append(s)
        
        return list(main_map.values())
