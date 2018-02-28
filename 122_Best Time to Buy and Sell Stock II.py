"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

""" 

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices:
            return profit
        
        buy_price = prices[0]
        
        for index,price in enumerate(prices[1:]):
            if price < prices[index]:
                profit += prices[index] - buy_price
                buy_price = price
            elif price > prices[index] and prices[index]<buy_price:
                buy_price = prices[index]
            
        return profit + max(prices[-1]-buy_price,0)