"""
Files - seek
"""

file = open("_test_files/example.txt", "r")
done = False
while True:
    line = file.readline()
    
    if len(line) == 0:
        break
    print(line, end="")

    if not done:
        print("FIRST LINE AGAIN")
        file.seek(0)
        done = True

file.close()
