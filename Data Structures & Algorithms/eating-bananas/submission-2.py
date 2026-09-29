class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        min_k = r = max(piles)
        while l <= r:
            k = l + (r - l)//2
            total_h = 0
            for p in piles:
                total_h += math.ceil(p/k)
            
            if total_h <= h:
                min_k = min(min_k, k)
                r = k - 1
            else:
                l = k + 1
        return min_k