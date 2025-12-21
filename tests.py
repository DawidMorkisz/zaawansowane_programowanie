import methods as m


def is_palonodrome_test():
    assert m.is_palindrome("kajak") == True
    assert m.is_palindrome("Kobyła ma mały bok") == True
    assert m.is_palindrome("python") == False
    assert m.is_palindrome("") == True
    assert m.is_palindrome("A") == True

