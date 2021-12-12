# You are climbing a stair case. It takes n steps to reach the top
# each time you can climb 1..k steps. You have also array which show you the red
# stairs. You are not allowed to get the red stair.
# How many distinct ways you can climb to the top

# 1. Define the objective function:
#   F(n), where n is number of stairs
# 2. Identify the base cases
#   F(0) = 0
# 3. Transition function
#   F(n) = F(n-1) + F(n -2) + ... + F(n - k)
# 4. Order of execution
#   Bottom-up
# 5. Location of the answer
#   F(n)


def climbingRedStairs(n: int, k: int, red: list):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j < 0:
                continue
            if i in red:
                dp[i] = 0
            else:
                dp[i] += dp[i - j]
    return dp[n]


print(climbingRedStairs(7, 3, [1, 3, 4]))
