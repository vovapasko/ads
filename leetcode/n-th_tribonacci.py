# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return n
        a = 0
        b = 1
        c = 1
        for i in range(2, n):
            tmp = a + b + c
            a = b
            b = c
            c = tmp
        return c
