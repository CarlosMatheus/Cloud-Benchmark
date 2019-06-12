from utils import *

install_geekbench()
install_application('sysbench')
install_application('stress-ng')

if not os.path.exists(dirName):
    os.mkdir(dirName)


def print_sep():
    print('===========================================================================================')


print_sep()
print('Note: 1 bogo ops is one iteration of what the test is doing')
print_sep()
print('Testing CPU with specific methods')
print_sep()
benchmark_call("stress-ng --cpu 1 --cpu-method sdbm --metrics-brief --perf -t 5", 'stress')
benchmark_call("stress-ng --cpu 1 --cpu-method int128decimal64 --metrics-brief --perf -t 5", 'stress')
benchmark_call("stress-ng --cpu 1 --cpu-method parity --metrics-brief --perf -t 5", 'stress')
benchmark_call("stress-ng --cpu 1 --cpu-method rand --metrics-brief --perf -t 5", 'stress')
benchmark_call("stress-ng --cpu 1 --cpu-method hamming --metrics-brief --perf -t 5", 'stress')
benchmark_call("stress-ng --cpu 1 --cpu-method matrixprod --metrics-brief --perf -t 5", 'stress')
print_sep()
print('Testing CPU using all metrics, each iteration is one metric and they are done in order')
print_sep()
benchmark_call("stress-ng --cpu 1 --cpu-method all --metrics-brief --perf -t 10", 'stress')
print_sep()
print('Testing the hd, each iteration is executed writes and reads')
print_sep()
benchmark_call("stress-ng --hdd 1  --metrics-brief --perf -t 10", 'stress')
print_sep()
print('Testing the memory, in which each iteration malloc(3), calloc(3), realloc(3) and  free(3).')
print_sep()
benchmark_call("stress-ng --vm 1 --vm-bytes 50% --vm-method all --verify -t 15 -v --metrics-brief --p", 'stress')
benchmark_call("sysbench --test=cpu --cpu-max-prime=100000 run", 'sysbench')
benchmark_call("./Geekbench-4.3.3-Linux/geekbench4", 'geekbench')
