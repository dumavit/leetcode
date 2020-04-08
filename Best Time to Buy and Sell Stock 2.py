class Solution(object):
    def maxProfit(self, prices):
        stock_price = None
        result = 0

        for i in range(0, len(prices)-1):
            price, next_price = prices[i], prices[i+1]
            if stock_price is None:
                if price < next_price:
                    # Buy stock
                    stock_price = price
            elif price > next_price:
                # Sell stock
                result += price - stock_price
                stock_price = 0

        if stock_price is not None:
            result += prices[-1] - stock_price
        return result


print(Solution().maxProfit([1, 2, 3, 4, 5]))
