import asyncio


async def greeting(delay=0.0):
    await asyncio.sleep(delay) 
    print(f"hey little hollywood:{delay}")

async def main():
    r = asyncio.gather(*[greeting(i) for i in range(5)])
    print("THER SHOW MUST GO ON")
    await asyncio.sleep(10)
    await r


if __name__ == "__main__":
    asyncio.run(main())


