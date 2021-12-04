# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(file_portfolio):
    """ 
    opens a given portfolio file and reads it into a list of dictionary.
    """
    n_stocks = []
    stock_prices = []
    portfolio = []

    with open(file_portfolio) as f :
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if row != [] :
                row_dict = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
                portfolio.append(row_dict)
    
    return portfolio

def read_prices(file_prices):
    """
    reads a set of prices from filename into a dictionary 
    where the keys of the dictionary are the stock names and 
    the values in the dictionary are the stock prices.
    """
    prices = {}

    with open(file_prices) as f :
        rows = csv.reader(f)
        for row in rows:
            if row != [] :
                prices[row[0]] = float(row[1])
            
    return prices

if len(sys.argv) == 3:
    file_portfolio = sys.argv[1]
    file_prices = sys.argv[2]
else:
    file_portfolio = 'Data/portfolio.csv'
    file_prices = 'Data/prices.csv'

list_stocks = read_portfolio(file_portfolio)
dict_prices = read_prices(file_prices)

old_value = sum([(stock['shares'] * stock['price']) for stock in list_stocks])
print(f"old value of portfolio = {old_value}")
new_value = sum([(stock['shares'] * dict_prices[stock['name']]) for stock in list_stocks])
print(f"current value of portfolio = {new_value}")
gain_or_loss = (new_value - old_value)
if (gain_or_loss > 0):
    print(f"gain = {gain_or_loss}")
else :
    print(f"loss = {-gain_or_loss}")
