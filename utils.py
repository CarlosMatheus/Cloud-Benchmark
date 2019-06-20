from subprocess import check_output
import requests
import os


URL = 'https://ipinfo.io/ip'
dirName = 'results'
results_file_extension = '.txt'


def print_sep_on_console(size):
    string = ''.join((['='] * size))
    print(string)


def print_title(iteration):
    title = "Iteration " + str(iteration) + " of " + str(NUM_ITERATIONS)
    print('\n\n\n')
    print_sep_on_console(len(title))
    print(title)
    print_sep_on_console(len(title))
    print('\n\n\n')


def create_folder():
    this_computer_name = input('What is this computer name? ')

    if not os.path.exists(dirName):
        os.mkdir(dirName)
    if not os.path.exists(os.path.join(dirName, this_computer_name)):
        os.mkdir(os.path.join(dirName, this_computer_name))
    return this_computer_name


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


def benchmark_call(command, benchmark_name, this_computer_name):
    call_command('echo Executing ' + benchmark_name, benchmark_name, this_computer_name)
    call_command("echo -------------------------------", benchmark_name, this_computer_name)
    call_command("date", benchmark_name, this_computer_name)
    res = call_command(command, benchmark_name, this_computer_name)
    if res is not None:
        print(benchmark_name + 'ended with code: ' + str(res))
    else:
        print(benchmark_name + 'ended')


def call_command(command, benchmark_name, this_computer_name):
    base_dir = os.path.join(dirName, this_computer_name)
    sufix = " 2>&1 | tee -a " + os.path.join(base_dir, benchmark_name + results_file_extension)
    return os.system(command + sufix)


def get_public_ip():
    try:
        ip = requests.get(URL).text[:-1]
    except:
        ip = None
    return ip
