# You are climbing a stair case. It takes n steps to reach the top
# each time you can climb 1..k steps.
# How many distinct ways you can climb to the top
def climb_k_steps(n: int, k: int):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        for j in range(1, k+1):
            if i - j < 0:
                continue
            dp[i] += dp[i-j]
    return dp[n]


print(climb_k_steps(5, 2))
print(climb_k_steps(5, 3))
print(climb_k_steps(40, 3))
