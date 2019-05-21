import os
from subprocess import check_output

dirName = 'results'
results_file_extension = '.txt'


def install_application(application_name):
    try:
        check_output([application_name, '--version'])
    except:
        print(application_name + ' not installed')
        print('installing ' + application_name + '...')
        os.system('apt-get install ' + application_name)


install_application('sysbench')
install_application('stress-ng')


if not os.path.exists(dirName):
    os.mkdir(dirName)

def benchmark_call(command, benchmark_name):
    print('Starting ' + benchmark_name)
    res = os.system(command + " > " + os.path.join(dirName, benchmark_name + results_file_extension))
    if res is not None:
        print(benchmark_name + 'ended with code: ' + res)
    else:
        print(benchmark_name + 'ended')


benchmark_call("./geekbench4", 'geekbench')
benchmark_call("sysbench --test=cpu --cpu-max-prime=50000 run", 'sysbench')
benchmark_call("stress-ng --cpu 1 --cpu-method matrixprod  --metrics-brief --perf -t 60", 'stress')
