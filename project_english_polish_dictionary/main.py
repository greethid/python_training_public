from resources.english_polish_dictionary import eng_pol_dict #to delete in future?
import resources.functions as f
import random


d = {'VENEZUELA':'CARACAS', 'CANADA':'OTTAWA'}
random.choice(list(d.values()))


if __name__ == '__main__':
    print(len(eng_pol_dict))
    copy_eng_pol_dict = eng_pol_dict.copy()
    word = eng_pol_dict.pop('Aborigine')
    print(word)
    print(len(eng_pol_dict))
    print(len(copy_eng_pol_dict))
    f.get_random_word()
    print(len(eng_pol_dict))
    f.start_game()
    print(f.username)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
