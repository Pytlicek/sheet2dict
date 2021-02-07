![Tests](https://github.com/Pytlicek/sheet2dict/workflows/Python%20package/badge.svg) [![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai) [![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# sheet2dict
A simple XLSX/CSV to dictionary converter

## Installing
To install the package from pip, first run:
```bash
python3 -m pip install --no-cache-dir sheet2dict
```

Required pip packages for sheet2doc: csv, openpyxl

## Usage
This library has 2 main features: reading a spreadsheet files and converting them to array of python dictionaries.  

### - XLSX
Use `xlsx_to_dict()` method  when converting form spreadsheets.  
Supported file formats for spreadsheets are: .xlsx,.xlsm,.xltx,.xltm  

```python3
# Import the library
from sheet2dict import Worksheet

# Create an object
ws = Worksheet()

# Convert 
ws.xlsx_to_dict(path='inventory.xlsx')

# object.headers() returns first row with the data in a spreadsheet 
print(ws.headers())

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
print(ws.headers())

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

# object.headers() returns first row with the data in a spreadsheet 
print(ws.headers())

# object.sheet_items returns converted rows as dictionaries in the array 
print(ws.sheet_items)
```
