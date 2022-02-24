# You are provided with two stack sequences, pushed and popped,
# with distinct values. Return true if and only if this could
# have been the result of a sequence of push and pop operations
# on an initially empty stack


def validate_stack_sequences(pushed: list, popped: list):
    # write your code here

    if len(pushed) != len(popped):
        return False
    i = 0
    stack = []
    for pid in pushed:
        stack.append(pid)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1

    if not stack:
        return True
    return False


validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
# have wrong behaviour in next line
validate_stack_sequences([1, 2, 3, 4, 5, 6, 7], [1, 2, 5, 3, 6, 7, 4])
