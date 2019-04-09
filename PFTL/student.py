from person import Person


class Student(Person):
    def __init__(self, name, last_name, course):
        super().__init__(name, last_name)
        self.course = course

    def is_enrolled_physics(self):
        if self.course == 'Physics':
            return True
        else:
            return False

    def generate_email(self):
        email = self.name + '.' + self.last_name + '@lmu.de'
        return email

s = Student('Aquiles', 'Carattino', 'Physics')
s.print_full_name()
print(s.course)
print(s.is_enrolled_physics())
print(s.birth_year)
s.birth_year = 1986
print(s.get_age())

s1 = Student('Aquiles', 'Carattino', 'Math')
print(s1.is_enrolled_physics())
s1.course = 'Physics'
print(s1.is_enrolled_physics())

email = s1.generate_email()
print(email)