# Quality-Adjusted Life-Year: https://open.kattis.com/problems/qaly
# Cosme M. Tejeda

N = int(input())
qaly = 0

for n in range(N):
    q, y = input().split()
    q = float(q)
    y = float(y)
    qaly += q * y

print(qaly)
