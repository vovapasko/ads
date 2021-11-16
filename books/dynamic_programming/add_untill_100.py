# The following function accepts an array of numbers and returns the sum, as long as a particular number doesn’t bring the sum above 100. If adding a particular number will make the sum higher than 100, that number is ignored. However, this function makes unnecessary recursive calls. Fix the code to eliminate the unnecessary recursion:

# def​ ​add_until_100​(array)
# ​ 	  ​return​ 0 ​if​ array.​length​ == 0
# ​ 	  ​if​ array[0] + add_until_100(array[1, array.​length​ - 1]) > 100
# ​ 	    ​return​ add_until_100(array[1, array.​length​ - 1])
# ​ 	  ​else​
# ​ 	    ​return​ array[0] + add_until_100(array[1, array.​length​ - 1])
# ​ 	  ​end​
# ​ 	​end​

# solution
def add_until_100(arr: list):
    if len(arr) == 0:
        return 0
    tmp = add_until_100(arr[1:])
    if arr[0] + tmp > 100:
        return tmp
    else:
        return arr[0] + tmp


print(add_until_100([20, 20, 40, 50]))
