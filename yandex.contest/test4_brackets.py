def get_variant(brackets_line, brackets_left):
    if max(brackets_left) == 0:
        yield brackets_line
    if brackets_left[0] > 0:
        yield from get_variant(brackets_line + '(', [brackets_left[0] - 1, brackets_left[1]])
    if brackets_left[1] > brackets_left[0]:
        yield from get_variant(brackets_line + ')', [brackets_left[0], brackets_left[1] - 1])


with open('input.txt', 'r') as fin:
    n = int(fin.readline())

with open('output.txt', 'w') as fout:
    for brackets_line in get_variant('', [n, n]):
        fout.write(brackets_line + '\n')

