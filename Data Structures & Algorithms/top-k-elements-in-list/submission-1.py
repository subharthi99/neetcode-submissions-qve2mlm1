from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a list which stores the elements in a fashion where the index represents the count of the occurence
        count_list = [[] for _ in range(len(nums) + 1)]
        map_counter = Counter(nums)
        # key: val -> num: freq
        # loop thru the dict and append nums at freq
        # store the freq of the nos in the list
        for num, freq in map_counter.items():
            count_list[freq].append(num)
        res = []
        # pop k number of times from the end
        for i in range(len(count_list)- 1, -1 , -1):
            for num in count_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return                
