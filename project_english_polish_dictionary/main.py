from resources.english_polish_dictionary import eng_pol_dict
import random
d = {'VENEZUELA':'CARACAS', 'CANADA':'OTTAWA'}
random.choice(list(d.values()))


def print_hi():
    print(copy_eng_pol_dict['Aborigine'])


def get_random_word():
    random_word = random.choice(list(eng_pol_dict.keys()))
    random_value = eng_pol_dict.pop(random_word)
    print(random_word)
    print(random_value)



if __name__ == '__main__':
    print(len(eng_pol_dict))
    copy_eng_pol_dict = eng_pol_dict.copy()
    word = eng_pol_dict.pop('Aborigine')
    print(word)
    print(len(eng_pol_dict))
    print(len(copy_eng_pol_dict))
    print_hi()
    get_random_word()
    print(len(eng_pol_dict))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
