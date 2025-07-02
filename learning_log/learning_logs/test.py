class Test():
    a = 1
    b = 'b'
    c = 60

    def __str__(self):
        return '__str__'

    def __repr__(self):
        return '__repr__'

    def __doc__(self):
        return '__doc__'

test = Test()

print(repr(Test))
print(test.__repr__())