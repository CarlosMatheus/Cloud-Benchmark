import os

dirName = 'results'
results_file_extension = '.txt'

if not os.path.exists(dirName):
    os.mkdir(dirName)


def benchmark_call(command, benchmark_name):
    print('Starting ' + benchmark_name + )
    os.system(command + " > " + os.path.join(dirName, benchmark_name + results_file_extension))


benchmark_call("./geekbench4", 'geekbench')
benchmark_call("sysbench --test=cpu --cpu-max-prime=50000 run", 'sysbench')
benchmark_call("stress-ng --cpu 1 --cpu-method matrixprod  --metrics-brief --perf -t 60", 'stress')
