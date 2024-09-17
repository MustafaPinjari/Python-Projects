import socket
from urllib.parse import urlparse

def get_hostname_ip():
    url = input("Enter the website URL: ")
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        if not hostname:
            hostname = url  # In case user enters a plain hostname without http/https
        print(f'Hostname : {hostname}')
        print(f'IP : {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'Invalid Hostname, error raised is {error}')

get_hostname_ip()