'''
https://docs.aiohttp.org/en/stable/web_quickstart.html

'''

from aiohttp import web
import aiohttp_cors

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class StaticServer:
    def run(self):
        app = web.Application()
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                    allow_credentials=True,
                    expose_headers="*",
                    allow_headers="*",
                )
        })
        route = app.router.add_static('/', 'public/')
        #cors.add(route)

        # https://github.com/aio-libs/aiohttp-cors/issues/151
        for resource in list(app.router.resources()):
            cors.add(resource)
        web.run_app(app)

if __name__ == "__main__":
    server = StaticServer()
    server.run()