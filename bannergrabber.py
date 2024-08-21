"""
bannergrabber.py: A program to fetch the banners of a computer's service on a port.
"""
import socket
import argparse
from types import NoneType


# grabber function creates a socket, connects and receives data from specific port on a host.
def grabber(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((address, int(port)))
        banner = sock.recv(1024)
        return banner
    # If we get Nonetype in our banner, continue with the program and print those as services not responding
    except ConnectionRefusedError:
         pass
    # Having firewall on causes OSError, pass and continue with our program.
    except OSError:
        pass
    finally:
        sock.close()

# Function to go through a loop of predefined ports one at a time, send this to the grabber function.
def port_number():
    ports = [20, 21, 22, 23, 443]
    successful_scan = ''
    failed_scan = []
    for port in ports:
        result = grabber(args.address, port)
        if type(result) == NoneType:
            failed_scan.append(result)
        else:
            successful_scan += f"[*]{result.decode()}"
    print(f'SUCCESSFUL SCAN RESULTS: \n{successful_scan}')
    print(f'SERVICES NOT RESPONDING: {len(failed_scan)}')

# Argument parser to run this program from command line.
parser = argparse.ArgumentParser(description='Scan ports for the provided IP')
parser.add_argument('-a', '--address', help='Provide IP address to scan')
args = parser.parse_args()

# Call port number function to do test
port_number()