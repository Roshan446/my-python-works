class Student:
    name:str
    roll_no:int
    course: str
    def set_stud(self, name, roll_no, crs):
        self.name = name
        self.roll_no = roll_no
        self.course = crs
    def display_std(self):
        print(self.name, self.roll_no, self.course)

std1 = Student()
std1.set_stud("manoj", 2, "django")
std2 = Student()
std2.set_stud("bilal", 3, "django")
std1.display_std()
std2.display_std()