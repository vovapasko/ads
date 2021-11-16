# Use recursion to write a function that accepts an array of numbers and returns
# a new array containing just the even numbers.

def get_even(arr: list, even: list = []):
    if len(arr) == 0:
        return even
    if arr[0] % 2 == 0:
        even.append(arr[0])
    return get_even(arr[1:], even)


print(get_even([1, 2, 3, 4], []))
print(get_even([], []))
print(get_even([1], []))
print(get_even([1, 3], []))
print(get_even([2], []))
print(get_even([2, 4], []))
