from pyais.stream import UDPStream
from src.duplicate_checker import DuplicateChecker
import logging
import settings


def udp_server(sync_q):
    checker = DuplicateChecker()

    for msg in UDPStream(settings.UDP_BIND, settings.UDP_PORT):
        decoded_message = msg.decode()

        if not checker.is_duplicate(decoded_message.nmea.raw):
            logging.debug("Received NMEA message: {}".format(decoded_message.nmea))
            sync_q.put(decoded_message)

    sync_q.join()
