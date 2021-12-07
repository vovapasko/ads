# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions[1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(version: int) -> bool:
    return version >= 4


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        right_index = n
        left_index = 1
        while right_index > left_index:
            m = int((right_index + left_index) / 2)
            bad_version = isBadVersion(m)
            if bad_version:
                right_index = m
            else:
                left_index = m + 1
        return left_index


s = Solution()
print(s.firstBadVersion(5))
