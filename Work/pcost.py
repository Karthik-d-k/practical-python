# pcost.py
#
# Exercise 1.27

n_stocks = []
stock_prices = []
Total_cost = 0

with open('Data/portfolio.csv', 'rt') as f :
    headers = next(f)
    for line in f:
        n_stocks.append(line.split(',')[1])
        stock_prices.append(line.split(',')[2].strip())
     
n_stocks = [int(n) for n in n_stocks]
stock_prices =  [float(p) for p in stock_prices]

Total_cost = sum([(n * p) for n, p in zip(n_stocks, stock_prices)])

print(f"{Total_cost=}")
