"""
Conditional means with observations

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from utils import get_tests_names


def integrate(lt):
    if type(lt) != type([]):
        lt = list(lt)
    for idx in range(1, len(lt)):
        lt[idx] += lt[idx - 1]
    return lt


def get_data_frame(lt):
    x_axis = [i for i in range(1, len(lt) + 1)]
    if type(lt) != type([]):
        hash_data_frame = {
            'x': x_axis,
            'y': list(lt),
        }
    else:
        hash_data_frame = {
            'x': x_axis,
            'y': lt,
        }
    return pd.DataFrame(hash_data_frame)


benchmark_names = ['stress', 'sysbench', 'client_ping', 'client_iperf3']
test_names = get_tests_names()
CSV_EXTENSION = '.csv'

sns.set()

treated_results_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'treated_results')

aws_path = os.path.join(treated_results_path, 'aws')
aws_unlimited_path = os.path.join(treated_results_path, 'aws_unlimited')
gc_path = os.path.join(treated_results_path, 'gc')
vm_path = os.path.join(treated_results_path, 'vm')


aws_stress_path = os.path.join(aws_path, 'stress' + CSV_EXTENSION)
aws_unlimited_stress_path = os.path.join(aws_unlimited_path, 'stress' + CSV_EXTENSION)
gc_stress_path = os.path.join(gc_path, 'stress' + CSV_EXTENSION)
vm_stress_path = os.path.join(vm_path, 'stress' + CSV_EXTENSION)

aws_stress_data = pd.read_csv(aws_stress_path)
aws_unlimited_stress_data = pd.read_csv(aws_unlimited_stress_path)
gc_stress_data = pd.read_csv(gc_stress_path)
vm_stress_data = pd.read_csv(vm_stress_path)
x_axis = [i for i in range(1, len(aws_stress_data.all_metrics)+1)]


# ==========================================


plt.plot(x_axis, aws_stress_data.all_metrics)
plt.plot(x_axis, gc_stress_data.all_metrics)
plt.plot(x_axis, vm_stress_data.all_metrics)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('all metrics test (bogo ops/s)')
plt.show()



plt.plot(x_axis, aws_stress_data.hd)
plt.plot(x_axis, gc_stress_data.hd)
plt.plot(x_axis, vm_stress_data.hd)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('hd test (bogo ops/s)')
plt.show()



plt.plot(x_axis, aws_stress_data.memory)
plt.plot(x_axis, gc_stress_data.memory)
plt.plot(x_axis, vm_stress_data.memory)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('memory test (bogo ops/s)')
plt.show()


aws_all_metrics = integrate(aws_stress_data.all_metrics)
gc_all_metrics = integrate(gc_stress_data.all_metrics)
vm_all_metrics = integrate(vm_stress_data.all_metrics)

plt.plot(x_axis, aws_all_metrics)
plt.plot(x_axis, gc_all_metrics)
plt.plot(x_axis, vm_all_metrics)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('all metrics test accumulated total (bogo ops)')
plt.show()

aws_hd = integrate(aws_stress_data.hd)
gc_hd = integrate(gc_stress_data.hd)
vm_hd = integrate(vm_stress_data.hd)

plt.plot(x_axis, aws_hd)
plt.plot(x_axis, gc_hd)
plt.plot(x_axis, vm_hd)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('hd test accumulated total (bogo ops)')
plt.show()


aws_memory = integrate(aws_stress_data.memory)
gc_memory = integrate(gc_stress_data.memory)
vm_memory = integrate(vm_stress_data.memory)

plt.plot(x_axis, aws_memory)
plt.plot(x_axis, gc_memory)
plt.plot(x_axis, vm_memory)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('Memory test accumulated total (bogo ops)')
plt.show()

# ==========================

aws_sysbench_path = os.path.join(aws_path, 'sysbench' + CSV_EXTENSION)
gc_sysbench_path = os.path.join(gc_path, 'sysbench' + CSV_EXTENSION)
vm_sysbench_path = os.path.join(vm_path, 'sysbench' + CSV_EXTENSION)

aws_sysbench_data = pd.read_csv(aws_sysbench_path)
gc_sysbench_data = pd.read_csv(gc_sysbench_path)
vm_sysbench_data = pd.read_csv(vm_sysbench_path)
x_axis = [i for i in range(1, len(aws_sysbench_data.sysbench_primes)+1)]

plt.plot(x_axis, aws_sysbench_data.sysbench_primes)
plt.plot(x_axis, gc_sysbench_data.sysbench_primes)
plt.plot(x_axis, vm_sysbench_data.sysbench_primes)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('sysbench primes test (bogo ops/s)')
plt.show()


aws_sysbench = integrate(aws_sysbench_data.sysbench_primes)
gc_sysbench = integrate(gc_sysbench_data.sysbench_primes)
vm_sysbench = integrate(vm_sysbench_data.sysbench_primes)

plt.plot(x_axis, aws_sysbench)
plt.plot(x_axis, gc_sysbench)
plt.plot(x_axis, vm_sysbench)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('sysbench primes test accumulated total (bogo ops/s)')
plt.show()

# ==========================

aws_client_ping_path = os.path.join(aws_path, 'client_ping' + CSV_EXTENSION)
gc_client_ping_path = os.path.join(gc_path, 'client_ping' + CSV_EXTENSION)
vm_client_ping_path = os.path.join(vm_path, 'client_ping' + CSV_EXTENSION)

aws_client_ping_data = pd.read_csv(aws_client_ping_path)
gc_client_ping_data = pd.read_csv(gc_client_ping_path)
vm_client_ping_data = pd.read_csv(vm_client_ping_path)
x_axis = [i for i in range(1, len(aws_client_ping_data.ping_mean)+1)]

plt.plot(x_axis, aws_client_ping_data.ping_mean)
plt.plot(x_axis, gc_client_ping_data.ping_mean)
plt.plot(x_axis, vm_client_ping_data.ping_mean)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('ping test (ms)')
plt.show()

#================================================


aws_client_ping = integrate(aws_client_ping_data.ping_mean)
gc_client_ping = integrate(gc_client_ping_data.ping_mean)
vm_client_ping = integrate(vm_client_ping_data.ping_mean)

plt.plot(x_axis, aws_client_ping)
plt.plot(x_axis, gc_client_ping)
plt.plot(x_axis, vm_client_ping)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('ping test accumulated total (ms)')
plt.show()


# =======================================================


plt.plot(x_axis, aws_unlimited_stress_data.all_metrics)
plt.plot(x_axis, gc_stress_data.all_metrics)
plt.plot(x_axis, vm_stress_data.all_metrics)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('all metrics test (bogo ops/s)')
plt.show()


plt.plot(x_axis, aws_unlimited_stress_data.hd)
plt.plot(x_axis, gc_stress_data.hd)
plt.plot(x_axis, vm_stress_data.hd)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('hd test (bogo ops/s)')
plt.show()


plt.plot(x_axis, aws_unlimited_stress_data.memory)
plt.plot(x_axis, gc_stress_data.memory)
plt.plot(x_axis, vm_stress_data.memory)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('memory test (bogo ops/s)')
plt.show()


aws_all_metrics = integrate(aws_unlimited_stress_data.all_metrics)
gc_all_metrics = integrate(gc_stress_data.all_metrics)
vm_all_metrics = integrate(vm_stress_data.all_metrics)

# sns.lmplot(data=get_data_frame(aws_all_metrics), x="x", y="y", markers=' ')
# sns.lmplot(data=get_data_frame(gc_all_metrics), x="x", y="y", markers=' ')
# sns.lmplot(data=get_data_frame(vm_all_metrics), x="x", y="y")
# plt.show()

plt.plot(x_axis, aws_all_metrics)
plt.plot(x_axis, gc_all_metrics)
plt.plot(x_axis, vm_all_metrics)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('all metrics test accumulated total (bogo ops)')
plt.show()

aws_hd = integrate(aws_unlimited_stress_data.hd)
gc_hd = integrate(gc_stress_data.hd)
vm_hd = integrate(vm_stress_data.hd)

plt.plot(x_axis, aws_hd)
plt.plot(x_axis, gc_hd)
plt.plot(x_axis, vm_hd)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('hd test accumulated total (bogo ops)')
plt.show()


aws_memory = integrate(aws_unlimited_stress_data.memory)
gc_memory = integrate(gc_stress_data.memory)
vm_memory = integrate(vm_stress_data.memory)

plt.plot(x_axis, aws_memory)
plt.plot(x_axis, gc_memory)
plt.plot(x_axis, vm_memory)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('Memory test accumulated total (bogo ops)')
plt.show()

# =========================================================================

# Get normal distributions

sns.kdeplot(aws_unlimited_stress_data.all_metrics, shade=True)
sns.kdeplot(gc_stress_data.all_metrics, shade=True)
plt.legend(['aws unlimited', 'gc'])
plt.xlabel('all metrics bogos ops/s')
plt.ylabel('distribution density')
plt.show()

sns.kdeplot(aws_client_ping_data.ping_mean, shade=True)
sns.kdeplot(gc_client_ping_data.ping_mean, shade=True)
plt.legend(['aws', 'gc'])
plt.xlabel('ping test (ms)')
plt.ylabel('distribution density')
plt.show()

sns.kdeplot(aws_unlimited_stress_data.hd, shade=True)
sns.kdeplot(gc_stress_data.hd, shade=True)
plt.legend(['aws unlimited', 'gc'])
plt.xlabel('HD bogos ops/s')
plt.ylabel('distribution density')
plt.show()

sns.kdeplot(aws_unlimited_stress_data.memory, shade=True)
sns.kdeplot(gc_stress_data.memory, shade=True)
plt.legend(['aws unlimited', 'gc'])
plt.xlabel('Memory bogos ops/s')
plt.ylabel('distribution density')
plt.show()
