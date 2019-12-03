from collections import Counter

with open('input.txt', 'r') as fin:
    str1 = fin.readline().rstrip()
    str2 = fin.readline().rstrip()

counts1 = sorted(Counter(str1).items())
counts2 = sorted(Counter(str2).items())

with open('output.txt', 'w') as fout:
    if counts1 == counts2:
        fout.write('1')
    else:
        fout.write('0')
