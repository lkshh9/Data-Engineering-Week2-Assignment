class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay=pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Lokesh', 'Kumawat', 60000)
emp_2 = Employee('Tyler', 'Durden', 5446)

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())

# print('{} {}'.format(emp_1.first, emp_1.last))
# each method within a class automatically takes the instance as first argument, and we're going to always
# call that self
