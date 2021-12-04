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
        for line_no, line in enumerate(f, start=1):
            try:
                n_stocks.append(int(line.split(',')[1]))
                stock_prices.append(float(line.split(',')[2]))
            except ValueError:
                print(f'Row {line_no}: Bad row: {line}')
    
    Total_cost = sum([(n * p) for n, p in zip(n_stocks, stock_prices)])
    
    return Total_cost

def portfolio_cost_using_csv(filename):
    """ 
    using csv builtin module to find total portfolio cost
    """
    nshares = 0
    price = 0
    Total_cost = 0

    with open(filename) as f :
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                Total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')         
    
    return Total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'
  
cost = portfolio_cost_using_csv(filename)
print('Total cost:', cost)
