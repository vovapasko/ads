# Write a function that accepts an array of strings and returns the first
# duplicate value it finds. For example, if the array is
# ["a", "b", "c", "d", "c", "e", "f"], the function should return "c",
# since it’s duplicated within the array. (You can assume that there’s one
# pair of duplicates within the array.) Make sure the function has an
# efficiency of O(N).

def get_duplicate(string_arr: list):
    string_dict = dict()
    for el in string_arr:
        value_unique = string_dict.get(el, True)
        if value_unique:
            string_dict[el] = False
        else:
            return el


print(get_duplicate(["a", "a"]))
print(get_duplicate(["b", "a", "b"]))
print(get_duplicate(["a", "b", "c", "d", "c", "e", "f"]))
