"""
Variable number of arguments
"""

def concat_spaced(*names):
    return_value = ""
    for n in names:
        return_value += n + " "
    print(return_value)

def my_sum(start, *numbers):
    for v in numbers:
        start += v
    print(start)

def mean(**grades): # dictionary params 
    sum_ = 0
    for name, grade in grades.items():
        concat_spaced(name, str(grade))
        sum_ += grade
    print("Mean: {:.2f}".format(sum_/len(grades)))

def both(*args, **kwargs):
    print(args)
    print(kwargs)

concat_spaced("Python", "101")
concat_spaced("Python", "is", "really", "great!")

print()
my_sum(0)
my_sum(4, 3)
my_sum(0, 3, 5, 4)

print()
mean(Student1=20, Student2=2)
print()
mean(Student1=20, Student2=2, Student3=15)

print()
both(1, 2, one='a', two='b')
