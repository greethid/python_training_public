class Employee(object):
    def __init__(self, name, last_name):
        if type(name) != str or type(last_name) != str:
            raise EmployeeError('Wrong argument given - name/surname not a string.')
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return self.name + ' ' + self.last_name

    def print_info(self):
        print("{} {}".format(self.name, self.last_name))

class EmployeeError(Exception):
    pass

try:
    e1 = Employee(1, 'Szymik')
except EmployeeError as e:
    print('Error occured: {}'.format(e))
else:
    print(e1)

def function(value_1, value_2):
    assert type(value_1) == int, "incorrect value given"
    return value_1 * value_2

print(function(3, 2))
print(function(2, 'f'))
# print(function('f', 2))
