'''
https://docs.aiohttp.org/en/stable/client_quickstart.html
'''

import aiohttp
import asyncio

import sys
import time


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(url):
    async with aiohttp.ClientSession() as session:
        #html = await fetch(session, 'http://python.org')
        html = await fetch(session, url)
        print(html)

url = sys.argv[1]
#print(url)
#time.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(url))
#loop.run_until_complete(main('http://google.com'))