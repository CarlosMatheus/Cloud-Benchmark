# Cloud benchmark

Checks the system and automatically installs the benchmark tools if they are not already installed. 

Then it wheels a series of benchmark tests with these tools and saves the results in text files inside the result folder.

After finishing the tests he does a compiled of these results and delivers you. 


## Will be using:

### Sysbench

It's open-source:
    https://github.com/akopytov/sysbench
    
### stress-ng

It's open-source:
    https://github.com/ColinIanKing/stress-ng

## Run

This application is only compatible with Ubuntu 18.04.

Run the file benchmark.py, it will install dependencies and run the benchmarks.

### Run cpu benchmark:

```bash
wget "https://github.com/CarlosMatheus/Cloud-Benchmark/archive/master.zip"
unzip master.zip
cd Cloud-Benchmark-master/
python3 cpu_benchmark.py
```

### Run io benchmark:

#### Server

```bash
python3 io_benchmark.py
```

Server will provide you the IP to connect in the client.
Remember to allow income connections on your firewall.

#### Client

```bash
python3 io_benchmark.py
```

Access using the server IP. If you are using a VirtualBox VM, set the Network as Bridge Adapter and use the VM private IP.

## Manual Installation

### Geekbench

```bash
wget "http://cdn.geekbench.com/Geekbench-4.3.3-Linux.tar.gz"
tar xf Geekbench-4.3.3-Linux.tar.gz
cd Geekbench-4.3.3-Linux/
./geekbench4
```

### sysbench

```bash
sudo apt-get install sysbench
sysbench --test=cpu --cpu-max-prime=20000 run
```

### stress-ng

```bash
sudo apt-get install stress-ng
stress-ng --cpu 1 --cpu-method matrixprod  --metrics-brief --perf -t 60
```

### iperf3

```bash
sudo apt-get install iperf3
```
