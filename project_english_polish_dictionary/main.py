"""Main module for english-polish dictionary project"""


import resources.functions as f


if __name__ == '__main__':
    f.start_game()
    f.load_game()

    while True:
        answer = f.ask_for_answer()
        if answer == 'q':
            break

    f.stop_game()











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
