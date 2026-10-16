class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        minprice=prices[0]
        for day in range(len(prices)):
            profit=prices[day]-minprice
            if profit > best:
                best=profit
            if minprice>prices[day]:
                minprice=prices[day]
        return best
            

