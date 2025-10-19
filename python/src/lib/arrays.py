def min_max(nums: list[int | float]) -> tuple[float | int, int | float]:
    if not isinstance(nums, list) or not len(nums):
        raise ValueError
    return min(nums), max(nums)
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if not isinstance(nums, list):
        raise ValueError
    return sorted(set(nums))
def flatten(mat: list[list | tuple]) -> list:
    if not all(isinstance(x, (list,tuple)) for x in mat) or not all(isinstance(x, (int,float)) for i in mat for x in i):
        raise ValueError
    return [x for i in mat for x in i]
