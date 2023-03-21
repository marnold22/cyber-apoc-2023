#!/usr/bin/env python3
import socket

with socket.socket() as connection:

    # initial connection to HTB
    connection.connect(('167.99.86.8', 32530))

    # Get start menu & send through 1 to initiate game
    print(connection.recv(4096).decode('utf-8'))
    connection.send(b'1')

    # Send rockpaperscissors 100 times
    for i in range(0, 100):
        print(connection.recv(4096).decode('utf-8'))
        connection.send(b'rockpaperscissors')

    # Recieve one extra time at the end to get the flag
    print(connection.recv(4096).decode('utf-8'))