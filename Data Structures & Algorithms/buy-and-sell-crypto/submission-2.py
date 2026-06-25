class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window where left and right pointers
        # global variable to track maxProfit
        # left = 0, right = 1

        # loop through right pointer in prices list
        # profit = prices[right] - prices[left]
        # if profit > 0
        # maxProfit = max(maxProfit, profit)
        # left = right

        # return maxProfit

        maxProfit = 0
        left = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                left = right

        return maxProfit