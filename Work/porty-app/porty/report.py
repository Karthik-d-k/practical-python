#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

from . import fileparse
from . import tableformat
from .stock import Stock
from .portfolio import Portfolio

def read_portfolio(file_portfolio, **opts):
    """
    opens a given portfolio file and reads it into a list of stock instances.
    """
    portfolio = []
    with open(file_portfolio) as lines:
        portfolio = Portfolio.from_csv(lines, **opts)

    return portfolio

def read_prices(file_prices):
    """
    reads a set of prices from filename into a dictionary
    where the keys of the dictionary are the stock names and
    the values in the dictionary are the stock prices.
    """
    prices = {}
    with open(file_prices) as lines:
        prices_list = fileparse.parse_csv(lines, types=[str, float], has_headers=False)
        prices = {k:v for k, v in prices_list}

    return prices

def make_report(list_stocks, dict_prices):
    """
    takes a list of stocks and dictionary of prices as input and returns a list of tuples
    containing the rows of Name, Shares, Price and Change.
    """
    name = [s.name for s in list_stocks]
    shares = [s.shares for s in list_stocks]
    price = [dict_prices[s.name] for s in list_stocks]
    change = [(dict_prices[s.name] - s.price) for s in list_stocks]

    return zip(name, shares, price, change)

def print_report(report, formatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def print_loss_or_gain(list_stocks, dict_prices):
    """
    prints out loss/gain.
    """
    old_value = sum([s.cost() for s in list_stocks])
    print(f"old value of portfolio = {old_value}")
    new_value = sum([(s.shares * dict_prices[s.name]) for s in list_stocks])
    print(f"current value of portfolio = {new_value}")
    gain_or_loss = (new_value - old_value)
    if (gain_or_loss > 0):
        print(f"gain = {gain_or_loss:>10.2f}\n")
    else:
        print(f"loss = {-gain_or_loss:>10.2f}\n")

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) < 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfoliofile pricefile')

    portfolio_filename = argv[1]
    prices_filename = argv[2]
    fmt = argv[3] if len(argv) == 4 else 'txt'
    portfolio_report(portfolio_filename, prices_filename, fmt)

if __name__ == '__main__':
    import sys
    main(sys.argv)
