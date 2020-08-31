# AIS Socket.IO Server
Listens for NMEA messages from rtl-ais via UDP and broadcasts them via Socket.IO

## Installation
1. Use `pipenv install` in order to pull the required packages.
2. Enjoy!

## Usage
1. Copy the included `.env.sample` file and name it `.env`.
2. Configure any required values.
3. Run the server using `pipenv run server.py`
4. This project contains a small script which reproduces dummy data captured in the port of Giurgiu, Romania. Should you
want to test the software, just run `pipenv run dummy_client.py`
5. Open the included webapp to see the live messages. (Defaults to http://localhost:5000, listens on all interfaces).
