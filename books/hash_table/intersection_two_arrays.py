# Write a function that returns the intersection of two arrays.
# The intersection is a third array that contains all values contained
# within the first two arrays. For example, the intersection of [1, 2, 3, 4, 5]
# and [0, 2, 4, 6, 8] is [2, 4]. Your function should have a complexity of O(N).

def intersection(array1: list, array2: list):
    array1_dict = {}
    for el in array1:
        array1_dict[el] = True
    intersection_array = []
    for el in array2:
        value = array1_dict.get(el, False)
        if value:
            intersection_array.append(el)
    return intersection_array
