from collections import Counter

def read_array(fin):
    line = fin.readline().split()
    k = int(line[0])
    array = [int(val) for val in line[1:]]

    return k, array

counter = Counter()
with open('input.txt') as fin:
    n = int(fin.readline())
    for _ in range(n):
        counter += Counter(map(int, fin.readline().split()[1:]))

with open('output.txt', 'w') as fout:
    for val, count in sorted(counter.items()):
        fout.write('{} '.format(val) * count)
