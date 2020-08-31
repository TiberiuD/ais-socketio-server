import asyncio
import janus
import logging
import sys
import settings

from src.udp_server import udp_server
from src.web_server import socketio_server


async def main():
    queue = janus.Queue()
    loop = asyncio.get_running_loop()
    fut = loop.run_in_executor(None, udp_server, queue.sync_q)
    await socketio_server(queue.async_q)
    await fut
    queue.close()
    await queue.wait_closed()

if __name__ == '__main__':
    # Logging configuration
    handlers = [
        logging.FileHandler(filename=settings.LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
    logging.basicConfig(
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        level=settings.LOG_LEVEL,
        handlers=handlers
    )

    # Run the app
    asyncio.run(main())
