def show_every_second_number(numbers):
    for number in range(0, len(numbers), 2):
        print(numbers[number])

numbers = list(range(1, 11))
show_every_second_number(numbers)