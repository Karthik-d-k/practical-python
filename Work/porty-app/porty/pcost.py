#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

from . import report

def portfolio_cost(filename):
    """
    using report.read_portfolio() to find total portfolio cost
    """
    portfolio = report.read_portfolio(filename)

    return portfolio.total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfoliofile')

    filename = argv[1]

    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
