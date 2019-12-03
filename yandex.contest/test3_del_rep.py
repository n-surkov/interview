with open('input.txt', 'r') as fin:
    with open('output.txt', 'w') as fout:
        n = int(fin.readline())
        if n != 0:
            prev_val = int(fin.readline())
            for i in range(n-1):
                val = int(fin.readline())
                if val != prev_val:
                    fout.write(str(prev_val) + '\n')
                    prev_val = val
            fout.write(str(prev_val))