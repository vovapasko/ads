
def generate_key(word) -> str:
    # converts "aabbc" to 26-element english alphabet list
    # [2, 2, 1, 0, 0, ..., 0]
    word_tuple = [0] * 26
    shift_index = 97
    for c in word:
        ascii_index = ord(c)
        intern_index = ascii_index - shift_index
        word_tuple[intern_index] += 1
    return str(word_tuple)


def group_anagrams(strs):
    # write your code here
    words_map = {}
    for word in strs:
        key = generate_key(word.lower())
        if key in words_map:
            words_map[key].append(word)
        else:
            words_map[key] = [word]
    anagrams = []
    for _, value in words_map.items():
        anagrams.append(value)
    return anagrams


print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
