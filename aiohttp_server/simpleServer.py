'''
https://docs.aiohttp.org/en/stable/web_quickstart.html

'''

from aiohttp import web

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class SimpleServer:
    def __init__(self):
        self.webpage_data = "Hello, world"

    async def send_webpage_data(self, request):
        return web.Response(text=self.webpage_data)

    async def recieve_webpage_data(self, request):
        data = await request.post()
        print("data:")
        print(data)
        # breaks if this doesn't exist in the post request
        self.webpage_data = data['webpage_data']
        return web.Response(text="Uploaded new data: {}".format(self.webpage_data))

    def run(self):
        app = web.Application()
        app.add_routes([web.get('/', self.send_webpage_data),
                    web.post('/', self.recieve_webpage_data)])
        web.run_app(app)

if __name__ == "__main__":
    server = SimpleServer()
    server.run()