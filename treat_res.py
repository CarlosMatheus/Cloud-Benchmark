import os

tests = ['aws', 'gc', 'vm']
dirName = 'treated_results'


def create_folder(test_name):
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    if not os.path.exists(os.path.join(dirName, test_name)):
        os.mkdir(os.path.join(dirName, test_name))


def write_results(test_name, benchmark_name, tests_names, results):
    create_folder(test_name)
    output_file = open('treated_results/' + test_name + '/' + benchmark_name + '.csv', 'w')
    output_file.write(','.join(tests_names) + '\n')

    for result in results:
        output_file.write(','.join(result) + '\n')


def treat_stress_result(test_name):

    def get_results_per_iter_per_test(iteration_texts_by_test_by_line):
        for i, iteration in enumerate(iteration_texts_by_test_by_line):
            for j, test in enumerate(iteration):
                if 'memory' not in test[0]:
                    iteration[j] = test[9]
                else:
                    iteration[j] = test[17]
                iteration[j] = iteration[j].split(']')[-1]
        return iteration_texts_by_test_by_line

    def get_results(results_per_iter_per_test):
        for iteration in results_per_iter_per_test:
            for idx, test in enumerate(iteration):
                iteration[idx] = list(filter(lambda a: a != '', test.split(' ')))[-2]
        return results_per_iter_per_test

    file = open('results/' + test_name + '/stress.txt', 'r')

    text = file.read()

    iteration_texts = text.split('Note: 1 bogo ops is one iteration of what the test is doing')
    del iteration_texts[0]

    iteration_texts_by_test = [m.split('Testing') for m in iteration_texts]
    iteration_texts_by_test = [m[1:] for m in iteration_texts_by_test]
    iteration_texts_by_test_by_line = [[m.split('\n') for m in n] for n in iteration_texts_by_test]

    results_per_iter_per_test = get_results_per_iter_per_test(iteration_texts_by_test_by_line)
    results = get_results(results_per_iter_per_test)

    tests_names = ['sdbm', 'int128decimal64', 'parity', 'rand',
                   'hamming', 'matrixprod', 'all_metrics', 'hd', 'memory']

    write_results(test_name, 'stress', tests_names, results)


def treat_sysbench_result(test_name):
    file = open('results/' + test_name + '/sysbench.txt', 'r')
    text = file.read()
    iteration_texts = text.split('Executing sysbench')
    del iteration_texts[0]
    iteration_texts_by_line = [n.split('\n') for n in iteration_texts]

    for idx, iteration in enumerate(iteration_texts_by_line):
        iteration_texts_by_line[idx] = iteration[18].split(':')[-1]
        iteration_texts_by_line[idx] = list(filter(lambda a: a != '', iteration_texts_by_line[idx].split(' ')))

    results = iteration_texts_by_line

    write_results(test_name, 'sysbench', ['sysbench_primes'], results)


for test in tests:
    treat_stress_result(test)
    treat_sysbench_result(test)

