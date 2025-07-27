class Solution(object):
    def maxProfit(self, prices):
        min_price = float("inf")
        maxprice = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > maxprice:
                maxprice = i - min_price
        return maxprice