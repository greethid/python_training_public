"""This file contains functions used in project english-polish dictionary"""


from resources.english_polish_dictionary import eng_pol_dict, copy_eng_pol_dict
from resources.BColors import BColors
import random
import json


#Variables
username = ''
correct_answers = 0
all_answers = 0


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
    print('Write polish translation for word which you see on the screen and press enter.'
          '\nPress "q" to quit.'
          '\nPress "s" for statistics.'
          '\nPress "r" for reset game.')


def ask_for_answer():
    """Ask user to give correct translation for word and delete that used word from dictionary"""
    global all_answers
    global correct_answers
    i = 0
    word = get_random_word()
    length = len(eng_pol_dict[word])
    answer = input(f'{word}: ')

    if answer == 'q':
        save_game()
        return answer

    while answer == 's' or answer == 'r' or answer == 'hard reset':
        if answer == 's':
            display_statistics()
        elif answer == 'r':
            reset_game()
        elif answer == 'hard reset':
            hard_reset_game()

        answer = input(f'{word}: ')

        if answer == 'q':
            save_game()
            return answer

    if answer in eng_pol_dict[word]:
        print(BColors.OKGREEN + 'OK' + BColors.ENDC)
        correct_answers += 1
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
    all_answers += 1


def display_statistics():
    """Display statistics of current game on the screen"""
    correct_percent = 0
    if all_answers > 0:
        correct_percent = correct_answers/all_answers * 100
    print(f'Correct answers: {correct_answers} out of {all_answers} which is {correct_percent:.0f} percent.')
    print(f'{len(eng_pol_dict)} words left.')


def stop_game():
    """Set of methods for game ending"""
    display_statistics()


def reset_game():
    """Reset current game statistics and start again"""
    global all_answers
    global correct_answers
    correct_percent = 0
    all_answers = 0


def hard_reset_game():
    """Reset all games statistics, saves and words answered"""
    global eng_pol_dict
    reset_game()
    # restore original dictionary
    eng_pol_dict = copy_eng_pol_dict.copy()


def save_game():
    """Save game progress (words used in dictionary) to file"""
    filename = 'save_file.json'
    with open(filename, 'w') as f:
        json.dump(eng_pol_dict ,f)
    pass


def load_game():
    """Load game progress (words used in dictionary) from file"""
    global eng_pol_dict
    filename = 'save_file.json'
    with open(filename, 'r') as f:
        eng_pol_dict = json.load(f)
