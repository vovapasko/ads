import asyncio


async def countdown(start: int):
    while start > 0:
        await asyncio.sleep(0.5)
        print("Down", start)
        start -= 1


async def countup(stop: int):
    i = 0
    while i < stop:
        await asyncio.sleep(1)
        print("Up", i)
        i += 1


async def main():
    res = await asyncio.gather(
        countup(10),
        countdown(5)
    )


asyncio.run(main())
