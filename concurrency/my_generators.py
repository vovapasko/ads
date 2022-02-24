def generator_play():
    global i

    def foo():
        i = 0
        while True:
            yield i
            i += 1

    def bar():
        yield 11
        yield 12

    res = foo()
    print(res)
    iter0 = res.__iter__()
    print(next(iter0))
    iter1 = res.__iter__()
    for i in range(10):
        print(next(iter1))
    for i in bar():
        print(i)


# generator_play()


def generator_exit():
    global gen

    def get_item():
        try:
            yield 5

        except GeneratorExit:
            print("GeneratorExit exception raised")

    gen = get_item()
    print(next(gen))
    print("Main exiting")


# generator_exit()


def generator_send():
    def generator_receiver():
        while True:
            received = yield
            print("received ", int(received))

    gen = generator_receiver()
    gen.__next__()
    for i in range(20, 30):
        gen.send(i)

    def generator_two_params():
        while True:
            par1, par2 = yield
            print(f"received {par1}, {par2}")

    gen2 = generator_two_params()
    gen2.__next__()
    for i in range(10):
        gen2.send(("a", 2))


generator_send()
