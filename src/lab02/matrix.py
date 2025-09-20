
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

#transpose
print("transpose")
print("[[1, 2, 3]] -> %s\n[[1], [2], [3]] -> %s\n[[1, 2], [3, 4]] -> %s\n[] -> %s" % (transpose([[1, 2, 3]]), transpose([[1], [2], [3]]), transpose([[1, 2], [3, 4]]), transpose([])))
try:
    transpose([[1,2], [3]])
except:
    print("[[1, 2], [3]] -> ValueError")
#row_sums
print("\nrows_sums")
print("[[1, 2, 3], [4, 5, 6]] -> %s\n[[-1, 1], [10, -10]] -> %s\n[[0, 0], [0, 0]] -> %s" % (row_sums([[1, 2, 3], [4, 5, 6]]), row_sums([[-1, 1], [10, -10]]), row_sums([[0, 0], [0, 0]])))
try:
    row_sums([[1,2], [3]])
except:
    print("[[1, 2], [3]] -> ValueError")
#col_sums
print("\ncol_sums")
print("[[1, 2, 3], [4, 5, 6]] -> %s\n[[-1, 1], [10, -10]] -> %s\n[[0, 0], [0, 0]] -> %s" % (col_sums([[1, 2, 3], [4, 5, 6]]), col_sums([[-1, 1], [10, -10]]), col_sums([[0, 0], [0, 0]])))
try:
    col_sums([[1,2], [3]])
except:
    print("[[1, 2], [3]] -> ValueError")
