import sys

n = int(sys.stdin.readline().strip())

max_subseq = 0
cur_subseq = 0
for i in range(n):
    el = int(sys.stdin.readline().strip())
    if el == 1:
        cur_subseq += 1
    else:
        if cur_subseq > max_subseq:
            max_subseq = cur_subseq
        cur_subseq = 0

if cur_subseq > max_subseq:
    max_subseq = cur_subseq

print(max_subseq)
