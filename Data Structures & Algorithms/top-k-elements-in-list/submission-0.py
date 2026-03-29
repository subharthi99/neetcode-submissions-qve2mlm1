class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## bucket sort
        ## create a list of lenghth nums - index represents the freq
        ## at worst the size of the 
        freq = [[] for i in range(len(nums) + 1)]
        cm = {}
        for i in nums:
            cm[i] = 1 + cm.get(i, 0)
        ## from the highest freq element - add it to the list 
        for num, cnt in cm.items():
            freq[cnt].append(num)
        ## then loop through the freq bucket list and keep popping until k is 0
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
