from utils import *

install_geekbench()
install_application('sysbench')
install_application('stress-ng')

if not os.path.exists(dirName):
    os.mkdir(dirName)

benchmark_call("./Geekbench-4.3.3-Linux/geekbench4", 'geekbench')
benchmark_call("sysbench --test=cpu --cpu-max-prime=100000 run", 'sysbench')
benchmark_call("stress-ng --cpu 1 --cpu-method matrixprod  --metrics-brief --perf -t 100", 'stress')
