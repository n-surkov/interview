import sys

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

j = set(j)
amount = 0
for br in j:
    amount += s.count(br)

print(amount)