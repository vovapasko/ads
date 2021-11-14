# almost works
def rotate(nums: list, k: int):
    rotated_list = [0] * len(nums)
    for i in range(len(nums)):
        new_index = i + k
        if new_index < len(nums):
            rotated_list[new_index] = nums[i]
        else:
            rotated_list[new_index - len(nums)] = nums[i]
    for i in range(len(nums)):
        nums[i] = rotated_list[i]
