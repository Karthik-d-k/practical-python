# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    """ 
    w/o using csv builtin module to find total portfolio cost
    """
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
    
    return Total_cost

def portfolio_cost_using_csv(filename):
    """ 
    using csv builtin module to find total portfolio cost
    """
    n_stocks = []
    stock_prices = []
    Total_cost = 0

    with open(filename) as f :
        rows = csv.reader(f)
        headers = next(rows)
        for line in rows:
            n_stocks.append(line[1])
            stock_prices.append(line[2])    
    
    n_stocks = [int(n) if n != '' else 0 for n in n_stocks]
    stock_prices =  [float(p) if p != '' else 0  for p in stock_prices]
    Total_cost = sum([(n * p) for n, p in zip(n_stocks, stock_prices)])
    
    return Total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
  
cost = portfolio_cost_using_csv(filename)
print('Total cost:', cost)
