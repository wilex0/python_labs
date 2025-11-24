import os, sys, csv
from src.lib.io_helper import check_path, ConvertTypes
from openpyxl import Workbook

from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str):
    csv_path, xlsx_path = check_path(csv_path, xlsx_path, ConvertTypes.CSV_TO_XLSX)
    print(xlsx_path)
    wb = Workbook()
    ws = wb.active
    ws.title = "WorkSpace1"
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in reader:
            ws.append(i)
        collinf = [
            (max(max(len(j.value), 8) for j in i), i[0].column_letter)
            for i in ws.columns
        ]
        for col in collinf:
            ws.column_dimensions[col[1]].width = col[0]
    wb.save(xlsx_path)


data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
p = Path("/home/wilex/Документы/GitHub/python_labs/python/data/samples/simple.csv")
with p.open("r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print({"age", "name"} <= set(rows[0].keys()))
print(set(data[0].keys()) == set(rows[0].keys()))
