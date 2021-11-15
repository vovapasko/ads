# Use recursion to write a function that accepts an array of strings and
# returns the total number of characters across all the strings.
# For example, if the input array is ["ab", "c", "def", "ghij"], the
# output should be 10 since there are 10 characters in total.

def rec_count(arr: list):
    if len(arr) == 0:
        return 0
    return len(arr[0]) + rec_count(arr[1:])


print(rec_count(["ab", "c", "def", "ghij"]))
print(rec_count(["ab"]))
print(rec_count(["abcdefghij"]))
print(rec_count([]))
print(rec_count([""]))
