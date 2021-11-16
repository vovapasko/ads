# Use recursion to write a function that accepts a string and returns
# the first index that contains the character “x.” For example, the string,
#  "abcdefghijklmnopqrstuvwxyz" has an “x” at index 23. To keep things simple,
#  assume the string definitely has at least one “x.”

def return_x(s: str, i=0):
    if s[0] == "x":
        return i
    return return_x(s[1:], i + 1)


print(return_x("abcdefghijklmnopqrstuvwxyz"))
