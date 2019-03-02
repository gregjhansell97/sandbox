'''
https://docs.aiohttp.org/en/stable/web_quickstart.html

'''

from aiohttp import web

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


webpageData = "Hello, world"

async def handler(request):
    return web.Response(text=webpageData)

async def post_handler(request):
    data = await request.post()
    print("data:")
    print(data)
    global webpageData
    webpageData = data['webpageData']
    return web.Response(text="Uploaded new data: {}".format(webpageData))

if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get('/', handler),
                web.post('/', post_handler)])
    web.run_app(app)