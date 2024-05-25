import datetime


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    '''
    Additional constructors

    @classmethod 
    def fromtimestamp(cls, t):
        
        Construct a date from a POSIX timestamp (like time.time()).
        y, m, d , hh, mm, ss, weekday, jday , dst = _time.localtime(t)
        
        return cls(y, m, d)

    @classmethod
    def today(cls):
        Construct a date from time.time().
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromordinal(cls, n):
        Construct a date from proleptic Gregorian ordinal.
        January 1 of year 1 is day 1. Only the year, month and day are non-zero in the result.
        
        y,m,d = _ord2ymd(n)
    '''


emp_1 = Employee('Lokesh', 'Kumawat', 620000)
emp_2 = Employee('Tyler', 'Durden', 655556)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Doe-90000'

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# print(new_emp_1.email)
# print(new_emp_1.pay)

new_emp_1 = Employee.from_string(emp_str_3)
# class method as alternative constructor,from_string is that alternative constructor
print(new_emp_1.email)
print(new_emp_1.pay)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

'''
lot of people gets class methods and static methods confused now when working with classes regular methods automatically 
pass the instance as the first argument and we call that self and class methods automatically pass the class as the first 
argument and we call that cls and static methods don't pass anything automatically they don't pass the instance or the class 
so really they behave just like regular functions except we include them in our classes because they have some logical connection 
with the class
'''
