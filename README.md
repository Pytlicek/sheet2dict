![Test Python package](https://github.com/Pytlicek/sheet2dict/workflows/Test%20Python%20package/badge.svg) 
[![codecov](https://codecov.io/gh/Pytlicek/sheet2dict/branch/main/graph/badge.svg?token=JL4BOX947I)](https://codecov.io/gh/Pytlicek/sheet2dict) 
![Upload Python Package to PyPI](https://github.com/Pytlicek/sheet2dict/workflows/Upload%20Python%20Package%20to%20PyPI/badge.svg) 
![PythonVersions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue) 
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai) 
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) 
[![Snyk](https://snyk-widget.herokuapp.com/badge/pip/sheet2dict/badge.svg)](https://snyk.io/advisor/python/sheet2dict) 
[![Downloads](https://pepy.tech/badge/sheet2dict)](https://pepy.tech/project/sheet2dict) 
[![Twitter Follow](https://img.shields.io/twitter/follow/Pytlicek?color=1DA1F2&logo=twitter&style=flat)](https://twitter.com/Pytlicek)


# sheet2dict
A simple XLSX/CSV reader - to dictionary converter  

## Installing
To install the package from pip, first run:
```bash
python3 -m pip install --no-cache-dir sheet2dict
```

Required pip packages for sheet2doc: csv, openpyxl

<p align="center"><img src="https://raw.githubusercontent.com/Pytlicek/sheet2dict/main/img/sheet2dict.gif?raw=true"/></p>

## Usage
This library has 2 main features: reading a spreadsheet files and converting them to array of python dictionaries.  

### - XLSX
Use `xlsx_to_dict()` method  when converting form spreadsheets.  
Supported file formats for spreadsheets are: .xlsx,.xlsm,.xltx,.xltm  
Spreadsheets with multiple worksheets are supported. If no sheet is specified, the active sheet is selected. If there is only one sheet, it is considered active.

```python3
# Import the library
from sheet2dict import Worksheet

# Create an object
ws = Worksheet()

# Convert active sheet (without specifying sheet name)
ws.xlsx_to_dict(path='inventory.xlsx')

# Convert the 'Main Warehouse' sheet of the 'inventory.xslx' spreadsheet file.
ws.xlsx_to_dict(path='inventory.xlsx', select_sheet='Main Warehouse')

# object.header returns first row with the data in a spreadsheet 
print(ws.header)

# object.sheet_items returns converted rows as dictionaries in the array 
print(ws.sheet_items)

```

You can parse data when worksheet is an object

```python3
# Import the library
from sheet2dict import Worksheet

# Example: read spreadsheet as object
path = 'inventory.xlsx'
xlsx_file = open(path, 'rb')
xlsx_file = BytesIO(xlsx_file.read())

# Parse spreadsheet from object
ws = Worksheet()
ws.xlsx_to_dict(path=xlsx_file)
print(ws.header)

```

### - CSV
Use `csv_to_dict()` method  when converting form csv.  
CSV is a format with many variations, better handle encodings and delimiters on user side and not within module itself.

```python3
# Import the library
from sheet2dict import Worksheet

# Create an object
ws = Worksheet()

# Read CSV file
csv_file = open('inventory.csv', 'r', encoding='utf-8-sig')

# Convert 
ws.csv_to_dict(csv_file=csv_file, delimiter=';')

# object.header returns first row with the data in a spreadsheet 
print(ws.header)

# object.sheet_items returns converted rows as dictionaries in the array 
print(ws.sheet_items)
```

### - Other functions
Worksheet **object.header** returns first row with the data in a spreadsheet 
```python
Python 3.9.1
[Clang 12.0.0 (clang-1200.0.32.28)] on darwin
>>> from sheet2dict import Worksheet
>>> ws = Worksheet()
>>> ws.xlsx_to_dict(path="inventory.xlsx")

>>> ws.header
{'country': 'SK', 'city': 'Bratislava', 'citizens': '400000', 'random_field': 'cc'}
```

Worksheet **object.sanitize_sheet_items** removes None or empty dictionary keys from `sheet_items`
```python
>>> from sheet2dict import Worksheet
>>> ws = Worksheet()
>>> ws.xlsx_to_dict(path="inventory.xlsx")

>>> ws.sheet_items
[
  {'country': 'CZ', 'city': 'Prague', 'citizens': '600000', None: '22', 'random_field': 'cc'},
  {'country': 'UK', 'city': 'London', 'citizens': '2000000', None: '33', 'random_field': 'cc'}
]

>>> ws.sanitize_sheet_items
[
  {'country': 'CZ', 'city': 'Prague', 'citizens': '600000', 'random_field': 'cc'},
  {'country': 'UK', 'city': 'London', 'citizens': '2000000', 'random_field': 'cc'}
]
```

# Contributing and Code of Conduct  
### Contributing to sheet2dict  
As an open source project, sheet2dict welcomes contributions of many forms.  
Please read and follow our [Contributing to sheet2dict](CONTRIBUTING.md)  

**Contributors:**
- Thanks to 白一百 (bái-yī-bǎi) for making sheet2dict work with multi-sheet Excel files.

### Code of Conduct  
As a contributor, you can help us keep the sheet2dict project open and inclusive.  
Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md)  
