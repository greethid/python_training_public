# Create a function, which takes range and returns list of
# square of odd integers from given range (do not use loops)
# Don't use loops (neither for nor while). List comprehensions are allowed.

def square_of_odd_integers(range_of_numbers):
    return [x**2 for x in range(range_of_numbers) if x % 2]


print(square_of_odd_integers(10))

# Create a function, which takes strings list and returns only those strings which start from letter "b".
# Don't use loops (neither for nor while). List comprehensions are allowed.
# Check this function on file three_rings.txt.

string_list = ['but', 'dom', 'balwan', 'kot', 'samochod', 'biedronka']


def string_start_from_b(words):
    return [word for word in words if word[0] == 'b']


print(string_start_from_b(string_list))


def get_all_words_from_text_file():
    with open('three_rings.txt', 'r') as text:
        all_file = text.read()
        return all_file.split()


def get_all_chars_from_text_file():
    with open('three_rings.txt', 'r') as text:
        all_file = text.read()
        return [char for char in all_file]


print(string_start_from_b(get_all_words_from_text_file()))

# print(get_all_chars_from_text_file())

# Create a function, which takes strings list and exchanges
# any letter "o" into "."
# Don't use loops (neither for nor while). List comprehensions are allowed.
# Check this function on file three_rings.txt.


def replace_o_into_dot(words):
    return [word.replace('o', '.') if 'o' in word else word for word in words]


print(replace_o_into_dot(string_list))
print(replace_o_into_dot(get_all_words_from_text_file()))
