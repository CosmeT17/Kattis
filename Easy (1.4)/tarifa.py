# Tarifa: https://open.kattis.com/problems/tarifa
# Cosme M. Tejeda

X = int(input())
N = int(input())
mb = X

for n in range(N):
    mb = mb - int(input()) + X
print(mb)
