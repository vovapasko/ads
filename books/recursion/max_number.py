def max(lst: list):
    print("recursion")
    if len(lst) == 1:
        return lst[0]
    if lst[0] > max(lst[1:]):
        return lst[0]
    return max(lst[1:])


print(max([1, 2, 3, 4]))
