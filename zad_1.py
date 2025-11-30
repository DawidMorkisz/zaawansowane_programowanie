class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50
    
student_1 = Student("Jan", [50, 80, 40])
student_2 = Student("Jan", [20, 40, 60])

print (student_1.is_passed())
print (student_2.is_passed())