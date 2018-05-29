"""
Files - readlines
"""

file = open("_test_files/example.txt", "r")

lines = file.readlines()
for line in lines:
    print(line, end="")

file.close()
