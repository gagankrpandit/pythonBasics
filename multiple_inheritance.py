class Employee:
    company = 'google'
    empCode = 62098
class Programmer:
    company = 'apple'
    empCode = 369874
class Freelancer(Employee, Programmer):
    name = 'gagan'

f = Freelancer()
print(f.empCode)
