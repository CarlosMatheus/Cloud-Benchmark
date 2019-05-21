# Cloud benchmark

## Instalation:

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

