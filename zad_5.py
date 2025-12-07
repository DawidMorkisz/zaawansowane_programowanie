def contains_value(values: list[int], number: int) -> bool:
    return number in values


print(contains_value([1, 2, 3, 4, 5], 3))
print(contains_value([1, 2, 3, 4, 5], 7))
