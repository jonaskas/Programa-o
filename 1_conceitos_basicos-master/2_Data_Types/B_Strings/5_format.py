"""
String format
- See: https://docs.python.org/3.6/library/string.html
- See: https://pyformat.info/
"""

message1 = "Python"
message2 = "Great"
print("Message1:{}, message2: {}".format(message1, message2))
print("Message1:{0}, message2: {1}".format(message1, message2))

print()
print("{0} is {1}, {0} IS {1}!!!!".format(message1, message2))
print("{m1} is {m2}, {m1} IS {m2}!!!!".format(m2=message2, \
                                              m1=message1))

print()
print(message1)
print(message2)
print(message1, end="")
print(message2)
print(message1, end=" ")
print(message2)

print()
print("1/3: {0}".format(1/3))
print("1/3: {0:f}".format(1/3))
print("1/3: {0:.3f}".format(1/3))
print("1/3: {0:10.3f}".format(1/3))
print("1/3: {0:010.3f}".format(1/3))

print()
print("{0:20} is GREAT".format(message1))
print("{0:>20} is GREAT".format(message1))
print("{0:^20} is GREAT".format(message1))

print()
print("{0:_<20} is GREAT".format(message1))
print("{0:_>20} is GREAT".format(message1))
print("{0:_^20} is GREAT".format(message1))

print("first: {0[0]};  second: {0[1]}".format(message1))
print("first: {0[0]};  second: {0[1]}".format([13, 24]))
