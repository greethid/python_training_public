"""This file contains functions used in project english-polish dictionary"""


from resources.english_polish_dictionary import eng_pol_dict
import random


#Variables
username = 'pies'


def get_random_word():
    random_word = random.choice(list(eng_pol_dict.keys()))
    random_value = eng_pol_dict.pop(random_word)
    print(random_word)
    print(random_value)
    return random_word


def start_game():
    # print("Welcome to the game for learning English!")
    # input("Please type your username and press enter: ")
    username = 'kot'
    print(username)