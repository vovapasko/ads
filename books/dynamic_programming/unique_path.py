def unique_path(m, n):
    return up(m, n, {})


def up(m, n, memo):
    if m == 1 or n == 1:
        return 1
    if memo.get(repr([m, n]), None) is None:
        memo[repr([m, n])] = up(m-1, n, memo) + up(m, n-1, memo)
    return memo[repr([m, n])]


print(unique_path(2, 3))
