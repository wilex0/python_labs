import pytest
import json
import csv

from src.lab05.json_csv import csv_to_json, json_to_csv
from src.lib.io_helper import write_csv, check_path_in


@pytest.mark.parametrize(
    "test, data, expected_length",
    [
        ("simple", [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}], 2),
        (
            "different_position",
            [{"name": "Alice", "age": 22}, {"age": 25, "name": "Bob"}],
            2,
        ),
        ("encodings", [{"name": "Алиса", "message": "Привет! 🌍"}], 1),
        ("empty_values", [{"name": "Alice", "age": 25, "comment": ""}], 1),
    ],
)
def test_json_to_csv_success(tmp_path, test, data, expected_length):
    src = tmp_path / f"{test}.json"
    dst = tmp_path / f"{test}.csv"

    src.write_text(json.dumps(data), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    assert dst.exists()
    with dst.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == expected_length
    assert set(data[0].keys()) == set(rows[0].keys())


@pytest.mark.parametrize(
    "test, data, expected_length",
    [
        ("basic", "name,age\nAlice,25\nBob,30", 2),
        ("special_chars", 'name,description\n"Alice","Test, comma"', 1),
        ("semicolon_delim", "name;age\nAlice;25\nBob;30", 2),
    ],
)
def test_csv_to_json_success(tmp_path, test, data, expected_length):
    src = tmp_path / f"{test}.csv"
    dst = tmp_path / f"{test}.json"

    src.write_text(data, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        json_dict = json.load(f)
    assert len(json_dict) == expected_length


@pytest.mark.parametrize(
    "test, data, expected_error",
    [
        (
            "uncorrect_header",
            [{"name": "Alice", "age": 25}, {"name": "Bob", "money": 10_000}],
            ValueError,
        ),
        ("file_not_found", None, FileNotFoundError),
        ("empty_file", "", ValueError),
        ("invalid_json", "{ invalid json }", ValueError),
    ],
)
def test_json_to_csv_errors(tmp_path, test, data, expected_error):
    src = tmp_path / f"{test}.json"
    dst = tmp_path / "data_out.csv"

    if data is None:
        with pytest.raises(FileNotFoundError, match="Файл не найден"):
            json_to_csv("uncorrected_file.json", str(dst))
    elif isinstance(data, list):
        src.write_text(json.dumps(data), encoding="utf-8")
    else:
        src.write_text(data, encoding="utf-8")

    with pytest.raises(expected_error):
        json_to_csv(str(src), str(dst))


@pytest.mark.parametrize(
    "test, data, expected_error",
    [
        ("file_not_found", None, FileNotFoundError),
        ("empty_file", "", ValueError),
        ("empty_header", "\nAlice,25", ValueError),
        ("empty_columns", "name,,age\nAlice,25,30", ValueError),
    ],
)
def test_csv_to_json_errors(tmp_path, test, data, expected_error):
    src = tmp_path / f"{test}.csv"
    dst = tmp_path / "data_out.json"

    if data is None:
        with pytest.raises(FileNotFoundError, match="Файл не найден"):
            json_to_csv("uncorrected_file.csv", str(dst))
    elif isinstance(data, list):
        src.write_text(json.dumps(data), encoding="utf-8")
    else:
        src.write_text(data, encoding="utf-8")

    with pytest.raises(expected_error):
        json_to_csv(str(src), str(dst))


def test_json_csv_roundtrip(tmp_path):
    data_json = tmp_path / "data_json.json"
    data_csv = tmp_path / "data_csv.csv"
    final = tmp_path / "final.json"

    data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    data_json.write_text(json.dumps(data), encoding="utf-8")

    json_to_csv(str(data_json), str(data_csv))
    csv_to_json(str(data_csv), str(final))
    with final.open("r", encoding="utf-8") as f:
        final_data = json.load(f)

    assert len(final_data) == 2
    assert set(final_data[0].values()) == {"Alice", "25"}


def test_json_to_csv_wrong_format(tmp_path):
    src = tmp_path / "data.dat"
    dst = tmp_path / "data_out.csv"

    src.write_text(
        '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]', encoding="utf-8"
    )

    with pytest.raises(ValueError, match="Некорректоный формат файла json/csv"):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_wrong_format(tmp_path):
    src = tmp_path / "data.dat"
    dst = tmp_path / "data_out.json"

    src.write_text("name,age\nAlice,25", encoding="utf-8")

    with pytest.raises(ValueError, match="Некорректоный формат файла csv/json"):
        csv_to_json(str(src), str(dst))


def test_csv_empty_to_json(tmp_path):
    src = tmp_path / "header.csv"
    dst = tmp_path / "test.json"

    src.write_text("name,age,county", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    assert dst.exists()

    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 0
