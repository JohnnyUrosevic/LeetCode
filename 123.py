class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # pre_profit[i] = max profit by making transaction before i
        pre_profits = [0] * len(prices)
        # post_profit[i] = max profit by making transaction after i
        post_profits = [0] * len(prices)
        
        min_price = prices[0]
        pre_profits[0] = 0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            pre_profits[i] = max(prices[i] - min_price, pre_profits[i-1])
        
        max_price = prices[-1]
        post_profits[-1] = 0
        for i in range(len(prices)-2, -1, -1):
            max_price = max(max_price, prices[i])
            post_profits[i] = max(max_price - prices[i], post_profits[i+1])
         
        max_profit = 0
        for split in range(len(prices)):
            transaction_1 = pre_profits[split]
            transaction_2 = post_profits[split]
        
            max_profit = max(max_profit, transaction_2 + transaction_1)
        
        return max_profit
