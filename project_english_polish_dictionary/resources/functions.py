"""This file contains functions used in project english-polish dictionary"""


from resources.english_polish_dictionary import eng_pol_dict
from resources.BColors import BColors
import random


#Variables
username = ''


def get_random_word():
    """Pick and return random word from dictionary"""
    random_word = random.choice(list(eng_pol_dict.keys()))
    return random_word


def start_game():
    """Welcome user and start game"""
    global username
    print('Welcome to the game for learning English!')
    username = input('Please type your username and press enter: ')
    print(f'Hello {username.title()}!')
    print('Write polish translation for word which you see on the screen and press enter. Press "q" to quit.')


def ask_for_answer():
    """Ask user to give correct translation for word and delete that used word from dictionary"""
    i = 0
    word = get_random_word()
    length = len(eng_pol_dict[word])
    answer = input(f'{word}: ')
    if answer in eng_pol_dict[word]:
        print(BColors.OKGREEN + 'OK' + BColors.ENDC)
    else:
        print(BColors.FAIL + 'NOK' + BColors.ENDC)
    for translation in eng_pol_dict[word]:
        if i >= length - 1:
            print(translation)
        else:
            print(translation, end=', ')
            i += 1
    # delete used word from dictionary
    del eng_pol_dict[word]


