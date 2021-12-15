# Given a string s, find the length of the longest substring
# without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sizes = [0]  # by default longest string so far is 0
        letter_map = {}
        l = 0
        for r in range(len(s)):
            if letter_map.get(s[r], None) is None:
                letter_map[s[r]] = r
            else:
                max_sizes.append(r - l)
                l = r
                letter_map = {s[l]: l}
        max_sizes.append(len(letter_map))
        return max(max_sizes)


s = Solution()
s.lengthOfLongestSubstring(" ")
