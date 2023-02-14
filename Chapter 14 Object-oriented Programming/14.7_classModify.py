# Lets say you have data with hundreds of attributes. You can create lists or
# dicts to store that data and refer to them. However, it can be incoveninet
# when dealing with 1000s of attributes and trying to find unique attributes 
# while also slcing and looping through them.
# OOP is particularly useful when handling data that requires multiple unique attributes.

# We create class of 3 attributes with one method which is get_grade

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade      # 0 - 100
    
    def get_grade(self):
        return self.grade

# We create another class which takes two attributes, but one of them is the previous class object
# This object will have 2 methods which is add student to course and get average grade.
# We also create a non-required attribute which is studentList

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.studentList = []

    def add_student(self, student):
        if len(self.studentList) < self. max_students:
            self.studentList.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.studentList: 
            value += student.get_grade()
        return (value/len(self.studentList))

# Define data of each unique student
s1 = Student("Tim", 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

# Create course object and add student object into it
science101 = Course("Science", 2)
science101.add_student(s1)
science101.add_student(s2)
science101.add_student(s3)

# Return the first student name
print(science101.studentList[0].name)

# Return grade average of course
print(science101.get_average_grade())

# Note that in this example, the amount of data and attributes is very limited where a
# simple list or dict could've sufficed. The point of this concept is to introduce the idea of how 
# O-OP requires more setup and code to get started but has greater potential for larger data sets.