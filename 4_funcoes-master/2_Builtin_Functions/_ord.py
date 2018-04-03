"""
ord
"""

def hash_me(text):
    hash_value = 0
    for e in text:
        hash_value += ord(e)
    return hash_value

def print_my_chars(text):
    for e in text:
        print(ord(e), end=" ")

message1 = "Python is Great!"
message2 = "Python is GREAT!"

print(hash_me(message1))
print(hash_me(message2))

print_my_chars(message1)
print()
print_my_chars(message2)
