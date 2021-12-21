# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(file_portfolio):
    """ 
    opens a given portfolio file and reads it into a list of dictionary.
    """
    portfolio = []

    with open(file_portfolio) as f :
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                row_dict = {'name' : record['name'], 'shares' : int(record['shares']), 'price' : float(record['price'])}
                portfolio.append(row_dict)
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
                
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

def make_report(list_stocks, dict_prices):
    """
    takes a list of stocks and dictionary of prices as input and returns a list of tuples 
    containing the rows of Name, Shares, Price and Change.
    """
    name = [stock['name'] for stock in list_stocks]
    shares = [stock['shares'] for stock in list_stocks]
    price = [dict_prices[stock['name']] for stock in list_stocks]
    change = [(dict_prices[stock['name']] - stock['price']) for stock in list_stocks]
    
    return zip(name, shares, price, change)

def print_report(report):
    """
    prints out the report.
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f"{'-' * 10} {'-' * 10} {'-' * 10} {'-' * 10}")
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {("$" + str(price)):>10s} {change:>10.2f}')

def print_loss_or_gain(list_stocks, dict_prices):
    """
    prints out loss/gain.
    """
    old_value = sum([(stock['shares'] * stock['price']) for stock in list_stocks])
    print(f"old value of portfolio = {old_value}")
    new_value = sum([(stock['shares'] * dict_prices[stock['name']]) for stock in list_stocks])
    print(f"current value of portfolio = {new_value}")
    gain_or_loss = (new_value - old_value)
    if (gain_or_loss > 0):
        print(f"gain = {gain_or_loss:>10.2f}\n")
    else:
        print(f"loss = {-gain_or_loss:>10.2f}\n")

def portfolio_report(portfolio_filename, prices_filename):
    """
    A top-level function for program execution.
    """
    list_stocks = read_portfolio(portfolio_filename)
    dict_prices = read_prices(prices_filename)
    print_loss_or_gain(list_stocks, dict_prices)
    report = make_report(list_stocks, dict_prices)
    print_report(report)

if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]
else:
    portfolio_filename = 'Data/portfoliodate.csv'
    prices_filename = 'Data/prices.csv'
    
portfolio_report(portfolio_filename, prices_filename)
