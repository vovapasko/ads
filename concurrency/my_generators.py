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


def get_item():
    try:
        yield 5

    except GeneratorExit:
        print("GeneratorExit exception raised")


gen = get_item()

print(next(gen))
print("Main exiting")
