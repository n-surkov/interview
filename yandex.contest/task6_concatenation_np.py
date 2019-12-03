import numpy as np


def read_array(fin):
    line = fin.readline().split()
    k = int(line[0])
    array = np.zeros((k, ), dtype=np.uint8)

    if k == 0:
        return k, array
    else:
        for i, val in enumerate(line[1:]):
            array[i] = int(val)

        return k, array


with open('input.txt') as fin:
    n = int(fin.readline())
    ks = np.zeros((n, ), dtype=np.uint8)
    matrix = np.full((n, 10 * n), 101, dtype=np.uint8)
    if n != 0:
        for i in range(n):
            k, array = read_array(fin)
            ks[i] = k
            matrix[i, :k] = array



with open('output.txt', 'w') as fout:
    if n != 0:
        for i in range(ks.sum()):
            min_idx = np.argmin(matrix[:, 0])
            fout.write('{} '.format(matrix[min_idx, 0]))
            matrix[min_idx, :-1] = matrix[min_idx, 1:]
    else:
        fout.write('')


