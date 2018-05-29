"""
Tuple
"""

def sum_and_len(values):
    sum_ = 0
    len_ = 0
    for year in values:
        for grade in year:
            if isinstance(grade, int) or isinstance(grade, float):
                len_ += 1
                sum_ += grade
    return (sum_, len_)

first_year = (15, 20)
second_year = (15, 20)
third_year = (10, ) * 3 
grades2 = (first_year, second_year, third_year) # tuple of tuples

sum, count = sum_and_len(grades2)
print("avg: ", sum / count)

_, count = sum_and_len(grades2)
print("counter: ", count)
