"""
for
"""

NUMBER = 17
hit = False

for attempt in range(5):
    if not hit:
        print("Attempt {}".format(attempt + 1))
        value = int(input("input a value: "))
        if value == NUMBER:
            print("Winner!!!")
            hit = True
        elif value > NUMBER:
            print("your number is greater")
        else:
            print("your number is lower")
