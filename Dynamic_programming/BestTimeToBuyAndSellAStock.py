class Solution(object):
    def maxProfit(self, prices):
        '''Brute Force Approach
        if len(prices)<=1: max_profit=0
        else: max_profit = prices[1] - prices[0]
        for j in range(1, len(prices)):
            for i in range(j):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max(max_profit, 0) '''
        
        max_profit = 0
        min_price_so_far = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price_so_far:
                min_price_so_far = prices[i]
            elif prices[i] - min_price_so_far > max_profit:
                max_profit = prices[i] - min_price_so_far
        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4]))