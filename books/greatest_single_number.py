def greatestNumber(array):
    greatest = array[0]
    for num in array:
        if num > greatest:
            greatest = num
    return greatest
