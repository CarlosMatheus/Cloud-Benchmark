from utils import *

install_application('iperf3')

SERVER = 's'
CLIENT = 'c'

this_computer_name = create_folder()


def call(command, benchmark_name):
    benchmark_call(command, benchmark_name, this_computer_name)


def client():
    print('You are defined as CLIENT')
    public_server_ip = input('What is the public server IP? ')
    call("iperf3 -c " + public_server_ip + ' -d', 'client_iperf3')
    call("ping " + public_server_ip + ' -t 8', 'client_ping')
    return 0


def server():
    print('You are defined as SERVER')
    public_server_ip = get_public_ip()
    if public_server_ip is not None:
        print('Your public IP is ' + public_server_ip)
    else:
        print('Failed to get your public IP address')
    print('Note: remember to allow income connections on your firewall')
    call("iperf3 -s", 'server_iperf3')
    return 0


operation_hash = {SERVER: server, CLIENT: client}

ans = ''
while ans != SERVER and ans != CLIENT:
    ans = input('Are you the client(c) or the server(s)?(c/s) ')

if not os.path.exists(dirName):
    os.mkdir(dirName)

function = operation_hash[ans]

function()
