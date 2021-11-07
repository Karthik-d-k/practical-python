# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):

    n_stocks = []
    stock_prices = []
    Total_cost = 0

    with open(filename, 'rt') as f :
        headers = next(f)
        for line in f:
            n_stocks.append(line.split(',')[1])
            stock_prices.append(line.split(',')[2].strip())    
    
    n_stocks = [int(n) if n != '' else 0 for n in n_stocks]
    stock_prices =  [float(p) if p != '' else 0  for p in stock_prices]

    Total_cost = sum([(n * p) for n, p in zip(n_stocks, stock_prices)])
    print(f"{n_stocks=} {stock_prices=}")
    
    return Total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
