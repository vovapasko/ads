# You are provided with two stack sequences, pushed and popped,
# with distinct values. Return true if and only if this could
# have been the result of a sequence of push and pop operations
# on an initially empty stack


def validate_stack_sequences(pushed: list, popped: list):
    # write your code here
    push_iter, popp_iter = 1, 0
    stack = [pushed[0]]
    try:
        while True:
            if stack[-1] == popped[popp_iter]:
                popp_iter += 1
                stack.pop()
            else:
                stack.append(pushed[push_iter])
                push_iter += 1
    except IndexError:
        return len(stack) == 0


validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
# have wrong behaviour in next line
validate_stack_sequences([1, 2, 3, 4, 5, 6, 7], [1, 2, 5, 3, 6, 7, 4])
