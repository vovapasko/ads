class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = self.get_min_len(word1, word2)
        new_word = ""
        for i in range(min_len):
            new_word += word1[i] + word2[i]
        if len(word1) == len(word2):
            return new_word
        if len(word1) > min_len:
            # first was bigger, need to concat the rest of it to the new word
            new_word += word1[min_len:]
        else:
            new_word += word2[min_len:]
        return new_word

    def get_min_len(self, word1, word2):
        if len(word1) < len(word2):
            return len(word1)
        return len(word2)
