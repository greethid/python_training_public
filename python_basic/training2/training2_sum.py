# Create a function calculating sum for any number of integers given to that function as arguments
# (don't use built-in function sum).

def sum_calculating(*args):
    sum_loc = 0
    for element in args:
        sum_loc += element
    return sum_loc


sum_cal = sum_calculating(10, 5, 7)

print(sum_cal)
