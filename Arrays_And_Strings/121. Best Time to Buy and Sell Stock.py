"""121. Best Time to Buy and Sell Stock """
"""TC: O(n)"""
"""SC: O(1)"""
prices = [7,1,5,3,6,2]
def bestbuy(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price=price

        profit = price - min_price

        if profit>max_profit:
            max_profit=profit
    return max_profit

print(bestbuy(prices))



