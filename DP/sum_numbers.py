# given n find the sum of 1 + 2+ 3 + ... + n

def sum_n(n: int):
    a = 1
    if n == 1:
        return 1
    for i in range(2, n + 1):
        tmp = a
        a = tmp + i
    return a


print(sum_n(5))
