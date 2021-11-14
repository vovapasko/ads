'''
Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist once—the
"n" and the "u", so your function should return the "n", since it occurs first.
The function should have an efficiency of O(N).
'''


def firstUnique(word: str):
    word_map = {}
    for el in word:
        if word_map.get(el, 0) == 0:
            word_map[el] = 1
        else:
            word_map[el] += 1
    for el in word:
        if word_map.get(el) == 1:
            return el


print(firstUnique("minimum"))
