# Two-sum: https://open.kattis.com/problems/twosum
# Cosme M. Tejeda

# Method 1 (0.045 sec) [FASTER!]

a, b = input().split()
a = int(a)
b = int(b)
print(a + b)

# Method 2 (0.05 sec)

a, b = [int(n) for n in input().split()]
print(a + b)
