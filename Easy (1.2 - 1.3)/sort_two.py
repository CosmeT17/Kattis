# Sort Two Numbers: https://open.kattis.com/problems/sorttwonumbers
# Cosme M. Tejeda

a, b = input().split()
a = int(a)
b = int(b)

if a < b: print(a, b)
else: print(b, a)
