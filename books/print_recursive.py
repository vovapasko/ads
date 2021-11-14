# Write a recursive function that prints all the numbers (and just numbers)

array = [1, 2, 3, [4, 5, 6], 7, [8, [9, 10, 11, [12, 13, 14]]], [
    15, 16, 17, 18, 19, [20, 21, 22, [23, 24, 25, [[26, 27], 29]], 30, 31], 32], 33]


def print_recursive(arr):
    for el in arr:
        if isinstance(el, list):
            print_recursive(el)
        else:
            print(el)


print_recursive(array)
