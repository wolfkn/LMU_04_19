class Person:
    def __init__(self, name, last_name, birth_year=0):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def print_full_name(self):
        print(self.name, self.last_name)

    def get_age(self):
        if self.birth_year == 0:
            raise Exception('The birth year was not provided')
        print('The age is:', 2019-self.birth_year)


# p = Person(name='Aquiles', last_name='Carattino', birth_year=1986)
# print(p.name)
# print(p.last_name)
# p.name = 'Juan'
# p.print_full_name()
# p.get_age()
#
# p1 = Person(name='John', last_name='Doe')
# print(p1.name)
# print(p1.last_name)
# p1.print_full_name()
# p1.birth_year = 1980
# p1.get_age()