class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxP = max(prices[r] - prices[l], maxP)
            r += 1
        return maxP
