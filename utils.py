import os
from subprocess import check_output

dirName = 'results'
results_file_extension = '.txt'


def install_geekbench():
    dir_name = 'Geekbench-4.3.3-Linux'
    if not os.path.exists(dir_name):
        os.system('wget "http://cdn.geekbench.com/Geekbench-4.3.3-Linux.tar.gz"')
        os.system('tar xf Geekbench-4.3.3-Linux.tar.gz')


def install_application(application_name):
    try:
        check_output([application_name, '--version'])
    except:
        print(application_name + ' not installed')
        print('installing ' + application_name + '...')
        os.system('sudo apt-get install ' + application_name)


def benchmark_call(command, benchmark_name):
    print('Starting ' + benchmark_name)
    # if 'eek' in benchmark_name:
    res = os.system(command + " |& tee " + os.path.join(dirName, benchmark_name + results_file_extension))
    if res is not None:
        print(benchmark_name + 'ended with code: ' + str(res))
    else:
        print(benchmark_name + 'ended')
    # else:
    #     res = check_output(command.split(' '))
    #     f = open(os.path.join(dirName, benchmark_name + results_file_extension), "w+")
    #     f.write(str(res))
    #     f.close()
    #     print(benchmark_name + 'ended')
