from utils import *

# install_geekbench()
install_application('sysbench')
install_application('stress-ng')

this_computer_name = create_folder()


def print_echo(string):
    call_command('echo ' + string, 'stress', this_computer_name)


def print_sep(size, file=True):
    string = ''.join((['='] * size))
    if file:
        print_echo(string)
    else:
        print(string)


def print_with_sep(string):
    print_sep(len(string))
    print_echo(string)
    print_sep(len(string))


def call(command, benchmark_name):
    benchmark_call(command, benchmark_name, this_computer_name)


num_iterations = int(input('What will be the number of iterations? '))

for i in range(num_iterations):
    print_title(i+1, num_iterations)
    print_with_sep('Note: 1 bogo ops is one iteration of what the test is doing')
    print('----------------------------')
    print_with_sep('Testing CPU method sdbm')
    call("stress-ng --cpu 1 --cpu-method sdbm --metrics-brief  -t 5", 'stress')
    print_with_sep('Testing CPU method int128decimal64')
    call("stress-ng --cpu 1 --cpu-method int128decimal64 --metrics-brief  -t 5", 'stress')
    print_with_sep('Testing CPU method parity')
    call("stress-ng --cpu 1 --cpu-method parity --metrics-brief  -t 5", 'stress')
    print_with_sep('Testing CPU method rand')
    call("stress-ng --cpu 1 --cpu-method rand --metrics-brief  -t 5", 'stress')
    print_with_sep('Testing CPU method hamming')
    call("stress-ng --cpu 1 --cpu-method hamming --metrics-brief  -t 5", 'stress')
    print_with_sep('Testing CPU method matrixprod')
    call("stress-ng --cpu 1 --cpu-method matrixprod --metrics-brief  -t 5", 'stress')
    print_with_sep('Testing CPU using all metrics, each iteration is one metric and they are done in order')
    call("stress-ng --cpu 1 --cpu-method all --metrics-brief  -t 10", 'stress')
    print_with_sep('Testing the hd, each iteration is executed writes and reads')
    call("stress-ng --hdd 1  --metrics-brief  -t 10", 'stress')
    print_with_sep('Testing the memory, in which each iteration malloc, calloc, realloc and free')
    call("stress-ng --vm 1 --vm-bytes 50% --vm-method all --verify -t 15 -v --metrics-brief", 'stress')
    call("sysbench --test=cpu --cpu-max-prime=100000 run", 'sysbench')
    # call("./Geekbench-4.3.3-Linux/geekbench4", 'geekbench')
