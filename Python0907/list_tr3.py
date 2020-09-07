total = 0
prices = [300, 200, 100, 500, 400]

for price in prices:
    total = total + price

print("Sum:" , total)

print("Cnt:" , len(prices))

ave = sum(prices) / len(prices)

print("Ave" , ave)