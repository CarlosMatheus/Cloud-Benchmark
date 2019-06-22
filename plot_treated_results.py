import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from utils import get_tests_names


test_names = get_tests_names()
CSV_EXTENSION = '.csv'
dirName = 'plots'
LINEAR = 'linear'
IO = 'io'
CPU = 'cpu'
DISTRIBUTION = 'density_distribution'
COMP_B = 'comparison_between'
AWS = 'aws'
AWS_UN = 'aws_unlimited'
GC = 'gc'
VM = 'vm'
LINEAR_AC = 'linear_accumulated'
MEM_VEL = 'memory_velocity'
HD_VEL = 'hd_velocity'
CPU_P_STR = 'cpu_perf_all_metrics_stressd'
PING = 'latency_time'
SYSB = 'sysbench'


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


def name(lt):
    return '_'.join(lt)


def save(p, file_name):
    p.savefig(file_name, bbox_inches='tight')


if not os.path.exists(dirName):
    os.mkdir(dirName)

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


# =====================================================================================================

# =======================================
# Non Accumulated stress results with aws
# =======================================

plt.plot(x_axis, aws_stress_data.all_metrics)
plt.plot(x_axis, gc_stress_data.all_metrics)
plt.plot(x_axis, vm_stress_data.all_metrics)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('all metrics test (bogo ops/s)')
save(plt, dirName + '/' + name([CPU, LINEAR, CPU_P_STR, COMP_B, VM, GC, AWS]))
plt.show()

# ===================================
# Non Accumulated hd results with aws
# ===================================

plt.plot(x_axis, aws_stress_data.hd)
plt.plot(x_axis, gc_stress_data.hd)
plt.plot(x_axis, vm_stress_data.hd)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('hd test (bogo ops/s)')
save(plt, dirName + '/' + name([IO, LINEAR, HD_VEL, COMP_B, VM, GC, AWS]))
plt.show()

# =======================================
# Non Accumulated memory results with aws
# =======================================

plt.plot(x_axis, aws_stress_data.memory)
plt.plot(x_axis, gc_stress_data.memory)
plt.plot(x_axis, vm_stress_data.memory)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('memory test (bogo ops/s)')
save(plt, dirName + '/' + name([IO, LINEAR, MEM_VEL, COMP_B, VM, GC, AWS]))
plt.show()

# ==================================================================================

# ============================
# Accumulated results with aws
# ============================

aws_all_metrics = integrate(aws_stress_data.all_metrics)
gc_all_metrics = integrate(gc_stress_data.all_metrics)
vm_all_metrics = integrate(vm_stress_data.all_metrics)

plt.plot(x_axis, aws_all_metrics)
plt.plot(x_axis, gc_all_metrics)
plt.plot(x_axis, vm_all_metrics)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('all metrics test accumulated total (bogo ops)')
save(plt, dirName + '/' + name([CPU, LINEAR_AC, CPU_P_STR, COMP_B, VM, GC, AWS]))
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
save(plt, dirName + '/' + name([IO, LINEAR_AC, HD_VEL, COMP_B, VM, GC, AWS]))
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
save(plt, dirName + '/' + name([IO, LINEAR_AC, MEM_VEL, COMP_B, VM, GC, AWS]))
plt.show()

# ===============================================================

# =========================================
# Non Accumulated sysbench results with aws
# =========================================

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
save(plt, dirName + '/' + name([CPU, LINEAR, SYSB, COMP_B, VM, GC, AWS]))
plt.show()

# =====================================
# Accumulated sysbench results with aws
# =====================================

aws_sysbench = integrate(aws_sysbench_data.sysbench_primes)
gc_sysbench = integrate(gc_sysbench_data.sysbench_primes)
vm_sysbench = integrate(vm_sysbench_data.sysbench_primes)

plt.plot(x_axis, aws_sysbench)
plt.plot(x_axis, gc_sysbench)
plt.plot(x_axis, vm_sysbench)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('sysbench primes test accumulated total (bogo ops/s)')
save(plt, dirName + '/' + name([CPU, LINEAR_AC, SYSB, COMP_B, VM, GC, AWS]))
plt.show()

# =================================================================

# =====================================
# Non Accumulated ping results with aws
# =====================================

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
save(plt, dirName + '/' + name([IO, LINEAR, PING, COMP_B, VM, GC, AWS]))
plt.show()

# =================================
# Accumulated ping results with aws
# =================================

aws_client_ping = integrate(aws_client_ping_data.ping_mean)
gc_client_ping = integrate(gc_client_ping_data.ping_mean)
vm_client_ping = integrate(vm_client_ping_data.ping_mean)

plt.plot(x_axis, aws_client_ping)
plt.plot(x_axis, gc_client_ping)
plt.plot(x_axis, vm_client_ping)
plt.legend(['aws', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('ping test accumulated total (ms)')
save(plt, dirName + '/' + name([IO, LINEAR_AC, PING, COMP_B, VM, GC, AWS]))
plt.show()

# ===================================================================

# ==========================================
# Non Accumulated results with aws unlimited
# ==========================================

plt.plot(x_axis, aws_unlimited_stress_data.all_metrics)
plt.plot(x_axis, gc_stress_data.all_metrics)
plt.plot(x_axis, vm_stress_data.all_metrics)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('all metrics test (bogo ops/s)')
save(plt, dirName + '/' + name([CPU, LINEAR, CPU_P_STR, COMP_B, VM, GC, AWS_UN]))
plt.show()


plt.plot(x_axis, aws_unlimited_stress_data.hd)
plt.plot(x_axis, gc_stress_data.hd)
plt.plot(x_axis, vm_stress_data.hd)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('hd test (bogo ops/s)')
save(plt, dirName + '/' + name([IO, LINEAR, HD_VEL, COMP_B, VM, GC, AWS_UN]))
plt.show()


plt.plot(x_axis, aws_unlimited_stress_data.memory)
plt.plot(x_axis, gc_stress_data.memory)
plt.plot(x_axis, vm_stress_data.memory)
plt.legend(['aws unlimited', 'gc', 'vm'])
plt.xlabel('iteration')
plt.ylabel('memory test (bogo ops/s)')
save(plt, dirName + '/' + name([IO, LINEAR, MEM_VEL, COMP_B, VM, GC, AWS_UN]))
plt.show()

# ======================================
# Accumulated results with aws unlimited
# ======================================

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
save(plt, dirName + '/' + name([CPU, LINEAR_AC, CPU_P_STR, COMP_B, VM, GC, AWS_UN]))
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
save(plt, dirName + '/' + name([IO, LINEAR_AC, HD_VEL, COMP_B, VM, GC, AWS_UN]))
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
save(plt, dirName + '/' + name([IO, LINEAR_AC, MEM_VEL, COMP_B, VM, GC, AWS_UN]))
plt.show()

# ========================
# Get normal distributions
# ========================

sns.kdeplot(aws_unlimited_stress_data.all_metrics, shade=True)
sns.kdeplot(gc_stress_data.all_metrics, shade=True)
plt.legend(['aws unlimited', 'gc'])
plt.xlabel('all metrics bogos ops/s')
plt.ylabel('distribution density')
save(plt, dirName + '/' + name([CPU, DISTRIBUTION, CPU_P_STR, COMP_B, GC, AWS_UN]))
plt.show()

sns.kdeplot(aws_client_ping_data.ping_mean, shade=True)
sns.kdeplot(gc_client_ping_data.ping_mean, shade=True)
plt.legend(['aws', 'gc'])
plt.xlabel('ping test (ms)')
plt.ylabel('distribution density')
save(plt, dirName + '/' + name([IO, DISTRIBUTION, PING, COMP_B, GC, AWS]))
plt.show()

sns.kdeplot(aws_unlimited_stress_data.hd, shade=True)
sns.kdeplot(gc_stress_data.hd, shade=True)
plt.legend(['aws unlimited', 'gc'])
plt.xlabel('HD bogos ops/s')
plt.ylabel('distribution density')
save(plt, dirName + '/' + name([IO, DISTRIBUTION, HD_VEL, COMP_B, GC, AWS_UN]))
plt.show()

sns.kdeplot(aws_unlimited_stress_data.memory, shade=True)
sns.kdeplot(gc_stress_data.memory, shade=True)
plt.legend(['aws unlimited', 'gc'])
plt.xlabel('Memory bogos ops/s')
plt.ylabel('distribution density')
save(plt, dirName + '/' + name([IO, DISTRIBUTION, MEM_VEL, COMP_B, GC, AWS_UN]))
plt.show()

# ==================================================
# Create io_bandwidth_comparison_between_clouds plot
# ==================================================

client_server_path = os.path.join(treated_results_path, 'gc_client_aws_server')
client_server_bandwidth_path = os.path.join(client_server_path, 'client_iperf3' + CSV_EXTENSION)

client_server_data = pd.read_csv(client_server_bandwidth_path)

gc_download_aws_upload = client_server_data.server_download
aws_download_gc_upload = client_server_data.server_upload

x_axis = [i for i in range(1, len(gc_download_aws_upload)+1)]

plt.plot(x_axis, gc_download_aws_upload)
plt.plot(x_axis, aws_download_gc_upload)
plt.legend(['gc download/aws upload', 'aws download/gc upload'])
plt.xlabel('iteration')
plt.ylabel('transmission rate (Mbps)')
save(plt, dirName + '/' + name([IO, LINEAR, 'bandwidth', COMP_B, GC, AWS_UN]))
plt.show()

