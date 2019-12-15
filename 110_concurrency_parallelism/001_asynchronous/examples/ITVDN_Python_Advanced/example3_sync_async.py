import asyncio
from asyncio.coroutines import iscoroutine
import time


def sync_worker(number, divider):
    print('Sync Worker started with values: {} / {}'.format(number, divider))
    time.sleep(1)
    print(number / divider)


@asyncio.coroutine
def async_worker(number, divider):
    print('Async Worker started with values: {} / {}'.format(number, divider))
    yield from asyncio.sleep(3)
    print(number / divider)


# sync
sync_worker(30, 10)
sync_worker(30, 10)

print(iscoroutine(sync_worker))
print(iscoroutine(async_worker(10, 2)))

# async
event_loop = asyncio.get_event_loop()
task_list = [
    event_loop.create_task(async_worker(30, 10)),
    event_loop.create_task(async_worker(50, 25)),
]
tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()
