# evaluate x ** 2 + 100 in coroutines chain for n natural numbers
import asyncio


async def add_me(x):
    result = x + 100
    return result


async def power_two(x):
    result = x ** 2
    result = await add_me(result)
    # yield from add_me(result)
    return result


async def equation(n):
    i = 1
    while i < n:
        result = await power_two(i)
        print(f"Number {i} result is {result}")
        # yield from power_two(i)
        i += 1


eq = equation(100)
loop = asyncio.get_event_loop()
loop.run_until_complete(eq)
