from utils import *

install_application('iperf3')

SERVER = 's'
CLIENT = 'c'

def client():
    print('You are defined as CLIENT')
    public_server_ip = input('What is the public server IP?')
    return 1


def server():
    print('You are defined as SERVER')
    public_server_ip = get_public_ip()
    if public_server_ip is not None:
        print('Your public IP is ' + public_server_ip)
    else:
        print('Failed to get your public IP address')
    print('Note: remember to allow income connections on your firewall')
    return 1


operation_hash = {SERVER: server, CLIENT: client}

ans = ''
while ans != SERVER and ans != CLIENT:
    ans = input('You are the client(c) or server(s)?')

function = operation_hash[ans]

function()
