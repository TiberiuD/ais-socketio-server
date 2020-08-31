import socketio
import asyncio
from aiohttp import web
from aiohttp_index import IndexMiddleware
import json
import logging
import settings


async def send_messages(sio, async_q):
    while True:
        message = await async_q.get()
        async_q.task_done()

        logging.debug(f"New message in queue: {message.nmea.raw}")

        # Repack the JSON
        nmea_json = json.dumps(json.loads(message.to_json()))

        await sio.emit('ais_rx', nmea_json)
        await asyncio.sleep(1)


@asyncio.coroutine
async def socketio_server(async_q):
    sio = socketio.AsyncServer()
    app = web.Application(middlewares=[IndexMiddleware()])
    sio.attach(app)

    @sio.event
    def connect(sid, environ):
        logging.info(f"New Socket.IO listener connected: {sid}")

    @sio.event
    def disconnect(sid):
        logging.info(f"New Socket.IO listener disconnected: {sid}")

    app.router.add_static('/', './data/website')

    # Serve the website & Socket.IO server
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, settings.WEB_BIND, settings.WEB_PORT)
    await site.start()

    # Start the message sender task
    task = asyncio.create_task(send_messages(sio, async_q))
