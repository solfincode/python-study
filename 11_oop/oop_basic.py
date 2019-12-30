class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def average(self):
        return sum(self.grades) / len(self.grades)

std1 = Student("David",(100,10,20,30,40))
print(std1.name)
print(std1.grades)
print(std1.average())