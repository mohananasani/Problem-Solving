class Solution:
    def maxProfit(self, prices):
        min= prices[0]
        max_profit= 0
        for i in range(len(prices)):
            # Keep the minimun value seen
            if prices[i]< min:
                min = prices[i]
            # Assume we have bought at min and now calc the profit with the current price- bought price
            profit = prices[i]-min
            if profit > max_profit:
                max_profit = profit
        return max_profit