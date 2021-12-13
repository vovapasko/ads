# Given a string s, find the length of the longest substring
# without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        symbols = {}
        counters = []
        counter = 0
        for el in s:
            if symbols.get(el, None) is None:
                symbols[el] = True
                counter += 1
            else:
                counters.append(counter)
                counter = 1
        counters.append(counter)
        return max(counters)


s = Solution()
s.lengthOfLongestSubstring(" ")
