# The following function uses recursion to calculate the Nth number from a mathematical sequence known as the “Golomb sequence.” It’s terribly inefficient, though! Use memoization to optimize it. (You don’t have to actually understand how the Golomb sequence works to do this exercise.)

# def​ ​golomb​(n)
# ​ 	  ​return​ 1 ​if​ n == 1
# ​ 	  ​return​ 1 + golomb(n - golomb(golomb(n - 1)))
# ​ 	​end​

def old_golomb(n):
    print("old")
    if n == 1:
        return n
    return 1 + old_golomb(n - old_golomb(old_golomb(n - 1)))


def golomb(n, memo):
    print("new")
    if n == 1:
        return n
    if memo.get(n, None) is None:
        memo[n] = 1 + golomb(n - golomb(golomb(n-1, memo), memo), memo)
    return memo[n]


print(old_golomb(10))
print(golomb(10, {}))
