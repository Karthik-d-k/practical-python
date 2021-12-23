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

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
