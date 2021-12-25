# tableformat.py
#
# Exercise 4.5

class TableFormatter:
    """
    An `abstract base class` for creating tables
    """
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Output data in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output data in csv format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    """
    create a formatter with given `name`
    """
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

    return formatter

def print_table(objects, columns, formatter):
    """
    Prints a table showing user-specified attributes of a list of arbitrary objects
    """
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in columns]
        formatter.row(rowdata)
