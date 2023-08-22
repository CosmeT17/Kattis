# Cudoviste: https://open.kattis.com/problems/cudoviste
# Cosme M. Tejeda

R, C = input().split()
R = int(R)
C = int(C)

# Cars Squashed: 0, 1, 2, 3, 4
count = [0, 0, 0, 0, 0]
cars_row = []

# First Line
line = input()
for c in range(C - 1):
        space_row = line[c:c+2]

        if '#' in space_row: 
             cars_row.append(-1)
        else: 
             cars_row.append(space_row.count('X'))

# Rest of Lines
for r in range(1, R):
    line = input()

    for c in range(C - 1):
        space_row = line[c:c+2]
        
        if '#' in space_row: 
             cars_row[c] = -1
        else:
            cars = space_row.count('X')
            if cars_row[c] != -1:
                count[cars_row[c] + cars] += 1
            cars_row[c] = cars

for num in count:
     print(num)
