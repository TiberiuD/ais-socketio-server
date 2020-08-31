import socket
import json
from time import sleep
import settings


with open("data/captured-messages.json") as dummyDataFile:
    dummyData = json.load(dummyDataFile)

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.connect((settings.DUMMY_UDP_SERVER_ADDR, settings.UDP_PORT))
    for message in dummyData:
        print("sending: {}".format(message["nmea"]["raw"]))
        bytesToSend = str.encode(message["nmea"]["raw"] + "\r\n")
        UDPClientSocket.sendall(bytesToSend)
        sleep(5)

    UDPClientSocket.close()
