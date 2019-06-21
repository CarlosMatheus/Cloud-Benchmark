file = open('results/aws/stress.txt', 'r')

text = file.read()

iteration_texts = text.split('Note: 1 bogo ops is one iteration of what the test is doing')
del iteration_texts[0]

iteration_texts_by_test = [m.split('Testing') for m in iteration_texts]
iteration_texts_by_test = [m[1:] for m in iteration_texts_by_test]
iteration_texts_by_test_by_line = [[m.split('\n') for m in n] for n in iteration_texts_by_test]


def get_results_per_iter_per_test(iteration_texts_by_test_by_line):
    for i, iteration in enumerate(iteration_texts_by_test_by_line):
        for j, test in enumerate(iteration):
            if 'memory' not in test[0]:
                iteration[j] = test[9]
            else:
                iteration[j] = test[17]
            iteration[j] = iteration[j].split(']')[-1]
    return iteration_texts_by_test_by_line


def get_result(results_per_iter_per_test):
    for iteration in results_per_iter_per_test:
        for idx, test in enumerate(iteration):
            iteration[idx] = list(filter(lambda a: a != '', test.split(' ')))[-2]
    return results_per_iter_per_test


results_per_iter_per_test = get_results_per_iter_per_test(iteration_texts_by_test_by_line)
result = get_result(results_per_iter_per_test)

print(result)
