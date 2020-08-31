from pyais.stream import UDPStream
from src.duplicate_checker import DuplicateChecker
import logging


def udp_server(sync_q):
    host = "0.0.0.0"
    port = 10110
    checker = DuplicateChecker()

    for msg in UDPStream(host, port):
        decoded_message = msg.decode()

        if not checker.is_duplicate(decoded_message.nmea.raw):
            logging.debug("Received NMEA message: {}".format(decoded_message.nmea))
            sync_q.put(decoded_message)

    sync_q.join()
