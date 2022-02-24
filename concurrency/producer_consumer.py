import asyncio
from asyncio import Future


async def produce(resource: Future):
    print("Start producing")
    await asyncio.sleep(1.5)
    print("Finished producing")
    resource.done()
    resource.set_result("---produced resource---")


async def consume(resource: Future):
    print("Waiting for resource")
    await resource
    print(f"Consumed resourse{resource.result()}")


async def main():
    future = Future()
    res = await asyncio.gather(produce(future), consume(future))

asyncio.run(main())
