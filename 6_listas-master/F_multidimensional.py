"""
Multidimensional
"""

data = [ [30, 15, 20], 
         [15, 37, 2], 
         [5, 26, 40] ]


for row in data:
    print()
    for c in row:
        print(c, end=" ")

print(data[0][1])

print()
for i in range(len(data)):
    print()
    for j in range(len(data[i])):
        print(data[i][j], end=" ")
