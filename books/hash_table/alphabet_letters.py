# Write a function that accepts a string that contains all the letters of
# the alphabet except one and returns the missing letter. For example,
# the string, "the quick brown box jumps over a lazy dog" contains all the
# letters of the alphabet except the letter, "f". The function should have a
# time complexity of O(N).
def get_letter(string: str):
    str_dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for el in string:
        str_dict[el] = True
    for letter in alphabet:
        if str_dict.get(letter, False) is False:
            return letter


print(get_letter("bcdefghijklmnopqrstuvwxyz"))
print(get_letter("the quick brown box jumps over a lazy dog"))
