class Person:
    country = 'India'
    def takeBreak(self):
        print('I am a person who is breathing...')
class Employee(Person):
    company = 'apple'
    def takeBreak(self):
        super().takeBreak()
        print('I am an employee and I am breathing...')
    def getCompany(self):
        print(f'The company is {self.company}')
class Programmer(Employee):
    designation = 'senior python developer'
    def takeBreak(self):
        super().takeBreak()
        print('I am a programmer and I am breathing...')
    def getDesignation(self):
        print(f'The designation is {self.designation}')

p = Person()
e = Employee()
prgmr = Programmer()
prgmr.takeBreak()
