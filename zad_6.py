def merge_and_transform(list1: list[int], list2: list[int]) -> list[int]:
    merged = list(set(list1 + list2))
    return [x ** 3 for x in merged]

print(merge_and_transform([1, 2, 3], [3, 4, 5]))