# a
def multiply_by_two_a(numbers):
    result = []
    for number in numbers:
        result.append(number*2)
    return result
#b
def multiply_by_two_b(numbers):
    return [number*2 for number in numbers]
     

numbers = [1, 2, 3, 4, 5]
print(multiply_by_two_a(numbers))
print(multiply_by_two_b(numbers))