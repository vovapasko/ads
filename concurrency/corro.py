import threading
import time
from collections import deque


class Scheduler:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, func):
        self.tasks.append(func)

    def run(self):
        while self.tasks:
            task = self.tasks.popleft()
            task()


scheduler = Scheduler()


def countdown(start: int):
    if start > 0:
        time.sleep(0.5)
        print("Down", start)
        scheduler.add_task(lambda: countdown(start - 1))


def countup(stop: int, i=0):
    if i < stop:
        time.sleep(1)
        print("Up", i)
        scheduler.add_task(lambda: countup(stop, i + 1))


scheduler.add_task(lambda: countdown(5))
scheduler.add_task(lambda: countup(5))

scheduler.run()
