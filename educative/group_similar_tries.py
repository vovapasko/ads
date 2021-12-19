# we need to determine how to individually group any character
# combination for a given title. Let’s imagine that our library
# has the following titles: "duel", "dule", "speed", "spede", "deul",
# "cars". You are tasked to design a functionality so that if a
# user misspells a word(for example speed as spede), they will still
# be shown the correct title.

from typing import Dict, List


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


def group_titles(strs: List[str]) -> Dict:
    # write your code here
    words_map = {}
    for word in strs:
        key = generate_key(word.lower())
        if key in words_map:
            words_map[key].append(word)
        else:
            words_map[key] = [word]
    return words_map


titles = ["duel", "dule", "speed", "spede", "deul", "cars"]
gt = group_titles(titles)
print(gt)
