class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        print(self.name, "is", self.age, "years old")

p = Person()

class Student(Person):
    def _init_(self, name, age, studentID): # Have to call the parent init because the attribute wasn't set
        self.studentID = studentID
        super()._init_(name, age)

    def enrol_into_uni(self):
        print("I am a student now")

    def get_studentID(self):
        print("My student ID is:", self.studentID)

s = Student()
s._init_("Jina", 5, 1234)
s.enrol_into_uni()
s.get_age()
s.get_studentID()