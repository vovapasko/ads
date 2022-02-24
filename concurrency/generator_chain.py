# evaluate x ** 2 + 100 in generators chain for n natural numbers

def add_me(x):
    result = x + 100
    yield result


def power_two(x):
    result = x ** 2
    yield add_me(result).__next__()
    # yield from add_me(result)

def equation():
    i = 1
    while True:
        yield power_two(i).__next__()
        # yield from power_two(i)
        i += 1


def start_gens(n):
    expr = equation()
    for i in range(n):
        print(f"Number {i} result is {expr.__next__()}")


start_gens(100)
