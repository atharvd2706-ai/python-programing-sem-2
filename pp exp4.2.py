def calculate_total(prices):
    total = sum(prices)
    return total


prices = [250, 499, 120, 300]

bill = calculate_total(prices)
print("Total Bill:", bill)