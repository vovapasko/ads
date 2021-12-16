# Given a string s, find the length of the longest substring
# without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = l = 0
        max_l = 0
        letter_map = {}
        while r < len(s):
            if letter_map.get(s[r], None) is None:
                letter_map[s[r]] = r
                r += 1
                max_l = max(max_l, r-l)
            else:
                del letter_map[s[l]]
                l += 1
        return max_l


s = Solution()
print(s.lengthOfLongestSubstring(" "))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("abca"))
