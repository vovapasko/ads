#Given an array of positive numbers, write a function that returns the greatest product of any three numbers. The approach of using three nested loops would clock in at O(N3), which is very slow. Use sorting to implement the function in a way that it computes at O(N log N) speed. (There are even faster implementations, but we’re focusing on using sorting as a technique to make code faster.)


def greatest_product(a: int, b: int, c: int):
    nums = [a, b, c]
    nums.sort()
    return nums[0] * nums[1] * nums[2]

print()