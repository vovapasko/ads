def generate_numbers():
    i = 0
    while True:
        i += 1
        yield i
        k = yield
        print("Received in generator function: " + str(k))


def generate_numbers_remastered():
    i = 0
    while True:
        i += 1
        k = (yield i)
        print("Received i in generator function remastered: " + str(k))


def send_events(callback):
    generator = callback()

    item = next(generator)
    print("Received in main script: " + str(item))

    # NOOP
    item = next(generator)
    print("Received in main script: " + str(item))

    item = generator.send(55)
    print("Received in main script: " + str(item))

    # NOOP
    item = next(generator)
    print("Received in main script: " + str(item))

    item = generator.send(65)
    print("Received in main script: " + str(item))

    # NOOP
    item = next(generator)
    print("Received in main script: " + str(item))

    item = generator.send(75)
    print("Received in main script: " + str(item))


if __name__ == "__main__":
    # send_events(generate_numbers)
    gen = generate_numbers_remastered()
    gen.__next__()
    for i in range(5):
        gen.send(i)

