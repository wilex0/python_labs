import csv, os.path


def read_text(path: str, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        content = f.read()
    return content


def write_csv(
    rows: list[tuple | list], path: str, header: tuple[str, ...] | None = None
):
    with open(path, "w", encoding="utf-8") as f:
        w = csv.writer(f)
        if header:
            w.writerow(header)
        rowsl = -1 if not rows else len(rows[0])
        if rowsl == -1:
            return
        elif any(len(x) != rowsl for x in rows):
            raise ValueError()
        w.writerows(rows)


def ensure_parent_dir(path: str):
    os.makedirs(path, exist_ok=True)
