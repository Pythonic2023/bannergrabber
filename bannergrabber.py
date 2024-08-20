"""
bannergrabber.py: A program to fetch the banners of a computer's service on a port.
"""
import socket
from types import NoneType


# TODO: Make grabber function which creates a socket, connects and receives data from specific port on a host.
def grabber(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((address, int(port)))
        banner = sock.recv(1024)
        return banner
    except ConnectionRefusedError:
         pass
    finally:
        sock.close()

grabber('127.0.0.1', 22)

# TODO: Function to go through a loop of predefined ports one at a time, send this to the grabber function.
def port_number():
    ports = [20, 21, 22, 23, 443]
    successful_scan = ''
    failed_scan = []
    for port in ports:
        result = grabber('127.0.0.1', port)
        if type(result) == NoneType:
            failed_scan.append(result)
        else:
            successful_scan += result.decode()
    print(f'SUCCESSFUL SCAN RESULTS: {successful_scan}')
    print(f'CONNECTION ERRORS: {len(failed_scan)}')
# TODO: Create an argument parser to run this program from command line.

# Call port number function to do test
port_number()