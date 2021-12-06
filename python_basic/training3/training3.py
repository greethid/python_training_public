class Employee(object):
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return self.name + ' ' + self.last_name

    def print_info(self):
        print("{} {}".format(self.name, self.last_name))

class Programmer(Employee):
    def __init__(self, name, last_name, position):
        self.position = position
        super(Programmer, self).__init__(name, last_name)

    def __str__(self):
        # return self.name + ' ' + self.last_name + ' ' + self.position
        name_surname = super(Programmer, self).__str__()
        return name_surname + ' is ' + self.position

class Manager(Programmer):
    pass

empl = Employee('Grzegorz', 'Szymik')
empl.print_info()
print(empl)
empl1 = Programmer('Grzegorz', 'Szymik', 'junior devops')
print(empl1)
empl2 = Manager('Grzegorz', 'Szymik', 'line manager')
print(empl2)

p1 = Programmer('Bob', 'Marley', 'junior devops')
p2 = Programmer('Bob', 'Marley', 'programmer')
p3 = Programmer('Bob', 'Marley', 'programmer')
m1 = Manager('Bob', 'Marley', 'LPO')
m2 = Manager('Bob', 'Marley', 'manager')
e1 = Employee('Regular', 'Employee')

class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def  __str__(self):
        return '\n'.join([str(emp) for emp in self.employee_list])

company = Company([p1, p2, p3, m1, m2, e1])
print(company)

class MulByN(object):
    def __init__(self, value):
        self.value = value

    def __mul__(self, value):
        return self.value * value

    # __rmul__ = __mul__

    def __rmul__(self, value):
        return self.value * value

num1 = MulByN(10)
print(num1 * 5)
print(7 * num1)
