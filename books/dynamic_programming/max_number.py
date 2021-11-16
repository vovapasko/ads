def max(lst: list):
    print("recursion")
    if len(lst) == 1:
        return lst[0]
    tmp = max(lst[1:])
    if lst[0] > tmp:
        return lst[0]
    return tmp


print(max([1, 2, 3, 4]))
