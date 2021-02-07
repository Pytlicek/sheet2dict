import sys
from pathlib import Path

sys.path.append(str(Path(".").absolute().parent))

from sheet2dict import Worksheet
from io import BytesIO


a = Worksheet()
a.xlsx_to_dict(path="inventory.xlsx")
print(">>", a.headers())
print(">>", a.sheet_items)


path = "inventory.xlsx"
xlsx_file = open(path, "rb")
xlsx_file = BytesIO(xlsx_file.read())

a = Worksheet()
a.xlsx_to_dict(path=xlsx_file)
print(">>", a.headers())


a = Worksheet()
path = "inventory.csv"
csv_file = open(path, "r", encoding="utf-8-sig")
a.csv_to_dict(csv_file=csv_file, delimiter=";")
print(">>", a.headers())
