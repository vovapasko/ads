def is_palindrome(word: str):
    reversed_word = ""
    for i in range(len(word), 0, -1):
        reversed_word += word[i - 1]
    return word == reversed_word


print(is_palindrome('madam'))
print(is_palindrome('eve'))
print(is_palindrome('Vova'))
