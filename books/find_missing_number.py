#The following function finds the “missing number” from an array of integers. 
# That is, the array is expected to have all integers from 0 up to the array’s length, 
# but one is missing.
#  As examples, the array, [5, 2, 4, 1, 0] is missing the number 3, and the array, 
# [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the number 8.

def missing_number(arr:list):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] - 1 != arr[i-1]:
            return arr[i] - 1
print(missing_number([5, 2, 4, 1, 0]))
print(missing_number([9, 3, 2, 5, 6, 7, 1, 0, 4]))

