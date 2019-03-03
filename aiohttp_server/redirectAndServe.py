'''
https://docs.aiohttp.org/en/stable/web_quickstart.html

'''

from aiohttp import web
#import aiohttp_cors

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Server:
    def __init__(self):
        with open('redirect.html', 'r') as myfile:
            # Make sure to escape by using double {{ and }}
            self.redirectTextUnformatted=myfile.read()

    async def send_redirect_data(self, request):
        redirectHost = "http://actualHost.com/"
        filePath = request.rel_url
        apparentHost = request.url.origin()
        redirectText = self.redirectTextUnformatted.format(redirectHost, filePath, apparentHost)
        return web.Response(headers={'Content-Type': 'text/html'}, body=redirectText)

    def run(self):
        app = web.Application()
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                    allow_credentials=True,
                    expose_headers="*",
                    allow_headers="*",
                )
        })
        app.router.add_static('/duckweb/', 'public/')
        app.add_routes([web.get('/{filePath}', self.send_redirect_data)])

        # https://github.com/aio-libs/aiohttp-cors/issues/151
        for resource in list(app.router.resources()):
           cors.add(resource)
        web.run_app(app)

if __name__ == "__main__":
    server = Server()
    server.run()