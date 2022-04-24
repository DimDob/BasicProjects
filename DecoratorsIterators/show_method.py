class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name


class Student(Person):
    def __init__(self, name, faculty_number):
        super().__init__(name)
        self.faculty_number = faculty_number

    def show(self):
        return f"Student has name: {self.name} and faculty number: {self.faculty_number}"


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show(self):
        return f"Teacher {self.name} has subject {self.subject}"


p = Person('Ivan')
s = Student('Kaloyan', 'f95532')
t = Teacher('Asen', 'mathematics')

print(p.show())
print(s.show())
print(t.show())