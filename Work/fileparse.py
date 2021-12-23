# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records.
    '''
    # safety check to avoid reading file names directly
    if isinstance(lines, (str, bytes)):
        raise RuntimeError(f"Pass in iterable after opening file.\nexample usage: parse_csv(open('{lines}'))")
    rows = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        # Read the file headers
        headers = next(rows)
    else:
        if select != None:
            # Exception gets raised if both the select and has_headers=False arguments are passed
            raise RuntimeError("select argument requires column headers")
    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows, start=1):
        if not row:    # Skip rows with no data
            continue
        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]
        # Apply type-conversions to data if specified
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not(silence_errors):
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue
        if has_headers:
            # Make a dictionary
            record = dict(zip(headers, row))
        else:
            # Make a tuple
            record = tuple(row)
        records.append(record)

    return records
