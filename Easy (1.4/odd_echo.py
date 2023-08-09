# Odd Echo: https://open.kattis.com/problems/oddecho
# Cosme M. Tejeda

N = int(input())
for n in range(1, N + 1):
    word = input()
    if n % 2 != 0:
        print(word)
