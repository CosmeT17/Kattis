# Chanukah Challenge: https://open.kattis.com/problems/chanukah
# Cosme M. Tejeda

P = int(input())
for p in range(P):
    k, N = input().split()
    k = int(k)
    N = int(N)
    print(k, int((N ** 2 + N) / 2 + N))
