#defineste studentul ESTE O CLASA

class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

# self - the actual object

#Obj Functions
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
