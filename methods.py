def is_palindrome(text: str) -> bool:
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n musi być >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def count_vowels(text: str) -> int:
    vowels = "aeiouyąęó"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("Discount musi być w zakresie 0–1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result += flatten_list(item)
        else:
            result.append(item)
    return result


def word_frequencies(text: str) -> dict:
    cleaned = ''
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned += char.lower()
    words = cleaned.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
