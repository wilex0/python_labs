def transpose(mat: list[list[float | int]]) -> list[list]:
    if not len(mat):
        return []
    if not all(isinstance(x, list) for x in mat) or not all(isinstance(x, (int,float)) for i in mat for x in i) or not all(len(x) == len(mat[0]) for x in mat):
        raise ValueError
    cnt_rows = len(mat); cnt_coll = len(mat[0])
    res = []
    for i in range(0, cnt_coll):
        new_row = []
        for j in range(0, cnt_rows):
            new_row.append(mat[j][i])
        res.append(new_row)
    return res

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not all(isinstance(x, list) for x in mat) or not all(isinstance(x, (int,float)) for i in mat for x in i) or not all(len(x) == len(mat[0]) for x in mat):
        raise ValueError
    return [sum(s) for s in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    return [sum(s) for s in transpose(mat)]
