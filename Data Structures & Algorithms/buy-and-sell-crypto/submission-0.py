class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buy = None
        
        for i in prices:
            if lowest_buy is None:
                lowest_buy = i
            else:
                if lowest_buy > i:
                    lowest_buy = i
                
                potential_profit = i - lowest_buy

                if potential_profit > max_profit:
                    max_profit = potential_profit

        return max_profit