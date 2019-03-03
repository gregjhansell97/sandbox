from aiohttp import web
import aiohttp_cors

import random
import sys

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Server:
    def __init__(self):
        with open('redirect.html', 'r') as myfile:
            # Make sure to escape by using double {{ and }}
            self.redirectTextUnformatted=myfile.read()
            self.redirectServers = ["http://localhost:8000", "http://localhost:8001", "http://localhost:8002", "http://localhost:8003"]            

    async def send_redirect_data(self, request):
        redirectHost = random.choice(self.redirectServers)
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
        
        # https://github.com/aio-libs/aiohttp-cors/issues/151
        for resource in list(app.router.resources()):
           cors.add(resource)

        app.add_routes([web.get('/{anyPath:.*}', self.send_redirect_data)])
        web.run_app(app, port=sys.argv[1])

if __name__ == "__main__":
    server = Server()
    server.run()