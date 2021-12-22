"""This file contains functions used in project english-polish dictionary"""


from resources.english_polish_dictionary import eng_pol_dict
import random


#Variables
username = ''


def get_random_word():
    random_word = random.choice(list(eng_pol_dict.keys()))
    return random_word


def start_game():
    global username
    print('Welcome to the game for learning English!')
    username = input('Please type your username and press enter: ')
    print(f'Hello {username.title()}!')
    print('Write polish translation for word which you see on the screen and press enter. Press "q" to quit.')


def ask_for_answer():
    i = 0
    word = get_random_word()
    length = len(eng_pol_dict[word])
    answer = input(f'{word}: ')
    if answer in eng_pol_dict[word]:
        print('OK')
    else:
        print('NOK')
    for translation in eng_pol_dict[word]:
        if i >= length - 1:
            print(translation)
        else:
            print(translation, end=', ')
            i += 1
    # delete used word from dictionary
    del eng_pol_dict[word]


