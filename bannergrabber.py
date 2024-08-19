"""
bannergrabber.py: A program to fetch the banners of a computer's service on a port.
"""
import socket

# TODO: Make grabber function which creates a socket, connects and receives data from specific port on a host.
def grabber(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((address, int(port)))
        print(f"Connected to {address} {port}")
        banner = sock.recv(1024)
        print(banner.decode())
    except Exception as e:
        print(f'Error in grabber function: {e}')
    finally:
        sock.close()

grabber('127.0.0.1', 22)

# TODO: Make a function to go through a loop of predefined ports one at a time, send this to the grabber function and receive our response.


# TODO: Create an argument parser to run this program from command line.