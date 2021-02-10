import sys
from pathlib import Path

sys.path.append(str(Path(".").absolute().parent))

from sheet2dict import Worksheet
from io import BytesIO


ws = Worksheet()
ws.xlsx_to_dict(path="inventory.xlsx")
print(">>", ws.header)
print("ALL:", ws.sheet_items)
print("SANITIZED:", ws.sanitize_sheet_items)


path = "inventory.xlsx"
xlsx_file = open(path, "rb")
xlsx_file = BytesIO(xlsx_file.read())

ws = Worksheet()
ws.xlsx_to_dict(path=xlsx_file)
print(">>", ws.header)


ws = Worksheet()
path = "inventory.csv"
csv_file = open(path, "r", encoding="utf-8-sig")
ws.csv_to_dict(csv_file=csv_file, delimiter=";")
print("ALL:", ws.sheet_items)
print("SANITIZED:", ws.sanitize_sheet_items)
