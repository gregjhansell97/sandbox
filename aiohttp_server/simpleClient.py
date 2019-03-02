'''
https://docs.aiohttp.org/en/stable/client_quickstart.html
'''

import aiohttp
import asyncio

import sys
import time

class SimpleClient:
    async def fetchGet(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def printGetRequest(self, url):
        async with aiohttp.ClientSession() as session:
            html = await self.fetchGet(session, url)
            print(html)

    async def fetchPost(self, session, url, postData):
        payload = {'webpage_data' : postData}
        async with session.post(url, data = payload) as response:
            return await response.text()

    async def printPostRequest(self, url, postData):
        async with aiohttp.ClientSession() as session:
            html = await self.fetchPost(session, url, postData)
            print(html)

    def getRequest(self, url):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.printGetRequest(url))

    def postRequest(self, url, postData):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.printPostRequest(url, postData))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        client = SimpleClient()
        client.getRequest(url)
    elif len(sys.argv) == 3:
        url = sys.argv[1]
        postData = sys.argv[2]
        client = SimpleClient()
        client.postRequest(url, postData)
    else:
        print("usage: {} url [postData]".format(sys.argv[0]))