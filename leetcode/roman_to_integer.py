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
    stack = [map.get(s[0])]
    if len(s) == 1:
        return stack.pop()
    for i in range(1, len(s)):
        num = map.get(s[i])
        last_el = stack[-1]
        if num > last_el:
            stack[-1] = num - last_el
        else:
            stack.append(num)
    return sum(stack)


print(romanToInt("V"))
print(romanToInt("III"))
print(romanToInt("VI"))
print(romanToInt("XXVI"))
print(romanToInt("IV"))
print(romanToInt("XIV"))
