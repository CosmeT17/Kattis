# Trik: https://open.kattis.com/problems/trik
# Cosme M. Tejeda

index = 1
moves = input()

# Method 1
for move in moves:
    if move == 'A':
        if index == 1: index = 2
        elif index == 2: index = 1

    elif move == 'B':
        if index == 2: index = 3
        elif index == 3: index = 2

    else:
        if index == 1: index = 3
        elif index == 3: index = 1

print(index)
