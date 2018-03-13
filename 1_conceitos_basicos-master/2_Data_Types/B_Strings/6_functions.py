"""
Functions
- See: help(str)
"""

message1 = "Python"
message2 = "Great"

print(message1, "is", message2) # print(*args)
print(message1 + " is " + message2) # concatenation
print("{} is {}".format(message1, message2)) # format

message = message1 + " is " + message2

print()
print("isnumeric:", message.isnumeric())
print("isnumeric:", "123".isnumeric())

print()
print("lower:", message.lower())
print("upper:", message.upper())
print("swap case:", message.swapcase())
print("capitalize:", message.capitalize())
print("title:", message.title())

print()
print("rjust:", message.rjust(25))
print("rjust:", message.rjust(25, "_"))
print("ljust:", message.ljust(25))
print("ljust:", message.ljust(25, "_"))
print("center:", message.center(25))
print("center:", message.center(25, "_"))

print()
print("zfill:", "3.14".zfill(10))
print("zfill:", "103.14".zfill(10))
print("zfill:", "3.1415161718".zfill(10))

print()
message = (message1 + " is great").upper()
print(message)

print()
print("Count py:", str(message.count("PY")))
print("Count py:", str(message.count("Py")))
print("Count t:", str(message.count("T")))

print()
print("Find T:", str(message.find("T")))
print("Find Z:", str(message.find("Z")))

print()
print("in:", str('Z' in message))

print()
print("Starts with P:", str(message.startswith("P")))
print("Ends with Z:", str(message.endswith("Z")))

print()
print("strip :" + " Python ".strip() + "|")
print("lstrip:" + " Python ".lstrip() + "|")
print("rstrip:" + " Python ".rstrip() + "|")

print()
print("Replace:", message.replace("GREAT", "Amazing"))

print()
print(">".join(['A', 'B', 'C', 'D']))
print(" ".join(['1', '2', '3', '4']))

print()
print("Student1;10;11;12".split(";"))

print()
# creates 3 partitions: before sep, sep and after sep
print("Team1 VS Team2".partition(" VS "))

print()
t1, t2, t3 = "Team1 VS Team2".partition(" VS ")
print(t1, t2, t3)
t1, _, t2 = "Team1 VS Team2".partition(" VS ") # throwaway var.
print(t1, t2)

print()
student = "Student1;10;11;12".partition(";")
print("name:{} grades:{}".format(student[0], student[2]))
