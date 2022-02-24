import inspect

var = None


def nested_generator():
    for _ in range(5):
        k = yield
        print("inner generator received = " + str(k))


def outer_generator():
    global var
    nested_gen = nested_generator()
    var = nested_gen
    next(nested_gen)

    for _ in range(5):
        k = yield
        try:
            nested_gen.send(k)
        except StopIteration:
            pass


if __name__ == "__main__":

    gen = outer_generator()
    next(gen)

    try:
        gen.close()
        print("Outer generator state: " + inspect.getgeneratorstate(gen))
        print("Inner generator state: " + inspect.getgeneratorstate(var))

    except StopIteration:
        pass
