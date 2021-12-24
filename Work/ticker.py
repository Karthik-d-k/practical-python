# ticker.py
#
# Exercise 6.10

import csv
import report
import tableformat
from follow import follow

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    """
    Creates a real-time stock ticker from a given portfolio, logfile, and table format
    """
    portfolio = report.read_portfolio(portfile)
    log_lines = follow(logfile)
    rows = parse_stock_data(log_lines)
    rows = filter_symbols(rows, portfolio)
    
    # Print it out
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])

# Example usage   
if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
