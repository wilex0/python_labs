import sys, os, json, csv
from src.lib.io_helper import check_path, ConvertTypes


def json_to_csv(json_path: str, csv_path: str):
    json_path, csv_path = check_path(json_path, csv_path, ConvertTypes.JSON_TO_CSV)
    with open(json_path, "r") as f:
        dirArr = json.load(f)
    header = dirArr[0].keys()
    if any(x.keys() != header for x in dirArr):
        raise ValueError("Ключи json не равны одному header")
    with open(csv_path, "w") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(dirArr)


def csv_to_json(csv_path: str, json_path: str):
    csv_path, json_path = check_path(csv_path, json_path, ConvertTypes.CSV_TO_JSON)
    with open(csv_path, "r") as f:
        read = list(csv.DictReader(f))
    with open(json_path, "w") as f:
        json.dump(read, f)
