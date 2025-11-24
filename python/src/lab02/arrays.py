def min_max(nums: list[int | float]) -> tuple[float | int, int | float]:
    if not isinstance(nums, list) or not len(nums):
        raise ValueError
    return min(nums), max(nums)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if not isinstance(nums, list):
        raise ValueError
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    if not all(isinstance(x, (list, tuple)) for x in mat) or not all(
        isinstance(x, (int, float)) for i in mat for x in i
    ):
        raise ValueError
    return [x for i in mat for x in i]


# min_max
print(
    f"min_max:\n[3, -1, 5, 5, 0] -> %s\n[42] -> %s\n[-5, -2, -9] -> %s\n[1.5, 2, 2.0, -3.1] -> %s"
    % (
        min_max([3, -1, 5, 5, 0]),
        min_max([42]),
        min_max([-5, -2, -9]),
        min_max([1.5, 2, 2.0, -3.1]),
    )
)
try:
    min_max([])
except ValueError:
    print("[] -> ValueError")

# unique_sorted
print(
    f"unique_sorted:\n[3, 1, 2, 1, 3] -> %s\n[] -> %s\n[-1, -1, 0, 2, 2] -> %s\n[1.0, 1, 2.5, 2.5, 0] -> %s"
    % (
        unique_sorted([3, 1, 2, 1, 3]),
        unique_sorted([]),
        unique_sorted([-1, -1, 0, 2, 2]),
        unique_sorted([1.0, 1, 2.5, 2.5, 0]),
    )
)

# flatten
print(
    f"flatten:\n[[1, 2], [3, 4]] -> %s\n([1, 2], (3, 4, 5)) -> %s\n[[1], [], [2, 3]] -> %s"
    % (
        flatten([[1, 2], [3, 4]]),
        flatten(([1, 2], (3, 4, 5))),
        flatten([[1], [], [2, 3]]),
    )
)
try:
    flatten([[1, 2], "ab"])
except ValueError:
    print('[[1, 2], "ab"] -> ValueError')
