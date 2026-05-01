class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = float('inf')
        sell_price = float('-inf')
        
        for i in range(len(prices)):

            buy_price = min(buy_price, prices[i])

            sell_price = max(sell_price, prices[i] - buy_price)

        return sell_price


        