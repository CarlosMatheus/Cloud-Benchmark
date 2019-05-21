# Cloud benchmark

Checks the system and automatically installs the benchmark tools if they are not already installed. 

Then it wheels a series of benchmark tests with these tools and saves the results in text files inside the result folder.

After finishing the tests he does a compiled of these results and delivers you.

## Run

This application is only compatible with Ubuntu 18.04.

Run the file benchmark.py, it will install dependencies and run the benchmarks.

```bash
wget "https://github.com/CarlosMatheus/Cloud-Benchmark/archive/master.zip"
unzip master.zip
cd Cloud-Benchmark-master/
python3 benchmark.py
```

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

