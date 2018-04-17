"""
Array of Class
"""

class Student():

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return "{}: {}".format(self.name, self.grade)

students = [ Student("Student1", 10), Student("Student2", 15), Student("Student3", 12), Student("Student4", 1) ]

students.append(Student("Student5", 20))

for item in students: 
    print(item)