# implement asyncio.sleep method without asyncio
import time
from collections import deque


class Scheduler:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def start(self):
        for task in self.tasks:
            try:
                task.__next__()
            except StopIteration:
                print("Finished")


scheduler = Scheduler()


def ping(n):
    for _ in range(n):
        time.sleep(0.5)
        print("ping")
        scheduler.add_task(lambda: ping(n-1))


def pong(n):
    for _ in range(n):
        time.sleep(0.5)
        print("pong")
        scheduler.add_task(lambda: pong(n-1))



#
ping_g = ping(5)
pong_g = pong(5)
# for i in range(5):
#     ping_g.__next__()
#     pong_g.__next__()
scheduler.add_task(ping_g)
scheduler.add_task(pong_g)
scheduler.start()
