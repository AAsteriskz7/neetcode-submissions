class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = 99999
        maxProfit = 0
        
        for price in prices:
            if price < lowestPrice:
                lowestPrice = price
            
            if price - lowestPrice > maxProfit:
                maxProfit = price - lowestPrice
        
        return maxProfit