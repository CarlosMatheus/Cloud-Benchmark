import os
from utils import *

dirName = 'results'
results_file_extension = '.txt'

install_geekbench()
install_application('sysbench')
install_application('stress-ng')

if not os.path.exists(dirName):
    os.mkdir(dirName)

benchmark_call("./geekbench4", 'geekbench')
benchmark_call("sysbench --test=cpu --cpu-max-prime=50000 run", 'sysbench')
benchmark_call("stress-ng --cpu 1 --cpu-method matrixprod  --metrics-brief --perf -t 60", 'stress')
