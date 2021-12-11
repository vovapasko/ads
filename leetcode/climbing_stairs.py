# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
# You are climbing a staircase. It takes n steps to reach the top.

class Solution:
    def climbStairsRecursion(self, n: int, memo={}) -> int:
        if n <= 2:
            return n
        return self.climbStairsRecursion(
            n-1) + self.climbStairsRecursion(n-2)

    def climbStairsMemo(self, n: int, memo={}) -> int:
        if n <= 2:
            return n
        if memo.get(n, None) is None:
            memo[n] = self.climbStairsMemo(n-1) + self.climbStairsMemo(n-2)
        return memo[n]

    def climbStairsDP(self, n: int):
        if n <= 2:
            return n
        first, second = 1, 1
        for _ in range(1, n):
            tmp = first
            first = second
            second = first + tmp
        return second


s = Solution()
print(s.climbStairsMemo(40))
print(s.climbStairsDP(40))
print(s.climbStairsRecursion(40))
