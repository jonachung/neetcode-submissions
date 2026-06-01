class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window ish where left = 0 right = 1 to len(prices)
        # while left < right
        # check profit (diff between right - left) and compare with global variable maxProfit
        #   if profit > 0 -> update maxProfit accordingly
        #.  else -> left = right
        #.  right += 1 regardless
        # update maxProfit occurdingly


        maxProfit = 0
        left = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1

        return maxProfit