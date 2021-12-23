#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

import sys
import report

def portfolio_cost(filename):
    """
    using report.read_portfolio() to find total portfolio cost
    """
    Total_cost = 0
    records = []

    records = report.read_portfolio(filename)
    Total_cost = sum([(record['shares'] * record['price']) for record in records])

    return Total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfoliofile')
        
    filename = argv[1]

    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
