def is_palindrome(x: int):
    x_str = str(x)
    i = 0
    j = len(x_str) - 1
    while i < j:
        if x_str[i] != x_str[j]:
            return False
        i += 1
        j -= 1
    return True


print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(2332))
print(is_palindrome(0))
print(is_palindrome(-1))
