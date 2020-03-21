import asyncio
from threading import Thread


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    t = Thread(target=loop.run_forever)
    t.start()
    print(loop.is_running())
    # loop is in another thread so thats how you stop it
    loop.call_soon_threadsafe(loop.stop)
    #loop.close()
    print("joining")
    t.join()
'''


async def main():
    while True

async def greeting(delay=0.0):
    await asyncio.sleep(delay) 
    print(f"hey little hollywood:{i}")

if __name__ == "__main__":

    x = asyncio.gather(*[greeting(i) for i in range(5)])
    print(x)
    asyncio.create_task(x)
    asyncio.run(asyncio.sleep(10))
    print("HERE")

'''
