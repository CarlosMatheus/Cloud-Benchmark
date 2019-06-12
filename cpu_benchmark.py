from utils import *

install_geekbench()
install_application('sysbench')
install_application('stress-ng')

if not os.path.exists(dirName):
    os.mkdir(dirName)


def print_echo(string):
    call_command('echo ' + string, 'stress')


def print_sep(size):
    print_echo(''.join((['=']*size)))


def print_with_sep(string):
    print_sep(len(string))
    print_echo(string)
    print_sep(len(string))


print_with_sep('Note: 1 bogo ops is one iteration of what the test is doing')
print('----------------------------')
print_with_sep('Testing CPU method sdbm')
benchmark_call("stress-ng --cpu 1 --cpu-method sdbm --metrics-brief  -t 5", 'stress')
print_with_sep('Testing CPU method int128decimal64')
benchmark_call("stress-ng --cpu 1 --cpu-method int128decimal64 --metrics-brief  -t 5", 'stress')
print_with_sep('Testing CPU method parity')
benchmark_call("stress-ng --cpu 1 --cpu-method parity --metrics-brief  -t 5", 'stress')
print_with_sep('Testing CPU method rand')
benchmark_call("stress-ng --cpu 1 --cpu-method rand --metrics-brief  -t 5", 'stress')
print_with_sep('Testing CPU method hamming')
benchmark_call("stress-ng --cpu 1 --cpu-method hamming --metrics-brief  -t 5", 'stress')
print_with_sep('Testing CPU method matrixprod')
benchmark_call("stress-ng --cpu 1 --cpu-method matrixprod --metrics-brief  -t 5", 'stress')
print_with_sep('Testing CPU using all metrics, each iteration is one metric and they are done in order')
benchmark_call("stress-ng --cpu 1 --cpu-method all --metrics-brief  -t 10", 'stress')
print_with_sep('Testing the hd, each iteration is executed writes and reads')
benchmark_call("stress-ng --hdd 1  --metrics-brief  -t 10", 'stress')
print_with_sep('Testing the memory, in which each iteration malloc, calloc, realloc and free')
benchmark_call("stress-ng --vm 1 --vm-bytes 50% --vm-method all --verify -t 15 -v --metrics-brief", 'stress')
benchmark_call("sysbench --test=cpu --cpu-max-prime=100000 run", 'sysbench')
benchmark_call("./Geekbench-4.3.3-Linux/geekbench4", 'geekbench')
