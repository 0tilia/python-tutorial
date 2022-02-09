# from the student file I want to import the Student class

from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.4, True)

print(student1.name)
print(student1.gpa)
print(student2.is_on_probation)
