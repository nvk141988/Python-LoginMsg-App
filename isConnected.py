import requests
import socket

REMOTE_SERVER = "one.one.one.one"
GOOGLE = "google.com"


def is_connected(hostname):
    try:
        # if u get a host name for remote server, that means dns resolved the address
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)  # Try to create a connection to TCP socket.
        s.close()  #
        return True
    except:
        pass
    return False


if is_connected(REMOTE_SERVER):
    print("Connected to Internet")
else:
    print("No Connected")
