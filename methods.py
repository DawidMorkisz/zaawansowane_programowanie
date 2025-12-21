from collections import Counter


# zad 1
def is_palindrome(text):
    return text == text[::-1]


# zad 2
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# zad 3
def count_vowels(string):
    vowels = set("aeiou")
    return sum(1 for char in string.lower() if char in vowels)


# zad 4
def calculate_discount(price, discount):

    return price * (1 - discount)


# zad 5
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


# zad 6
def word_frequencies(text):
    words = text.split()
    return Counter(words)


# zad 7
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
