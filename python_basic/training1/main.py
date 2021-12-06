# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

with open('three_rings.txt', 'r') as text:
    all_file = text.read()

    without_dots = all_file.replace('.', '')
    without_comas = without_dots.replace(',', '')
    same_case = without_comas.upper()
    words = same_case.split()
    set_ready = set(words)

    print(set_ready)
    print(type(set_ready))
