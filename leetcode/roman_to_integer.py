def romanToInt(s: str):
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if len(s) == 1:
        return map[s]
    res = 0
    for i in range(1, len(s)):
        curr = map[s[i]]
        prev = map[s[i - 1]]
        if curr > prev:
            res += (curr - prev)
        else:
            res += curr
