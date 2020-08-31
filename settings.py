import os
from dotenv import load_dotenv
load_dotenv()

UDP_BIND = os.getenv("UDP_BIND", "127.0.0.1")
UDP_PORT = int(os.getenv("UDP_PORT", 10110))

DUMMY_UDP_SERVER_ADDR = os.getenv("DUMMY_UDP_SERVER_ADDR", "127.0.0.1")

WEB_BIND = os.getenv("WEB_BIND", "127.0.0.1")
WEB_PORT = int(os.getenv("WEB_PORT", 5000))

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
LOG_FILE = os.getenv("LOG_FILE", "log/server.log")
