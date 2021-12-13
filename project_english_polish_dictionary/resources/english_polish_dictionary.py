"""This file contains english-polish dictionary, english words as keys of dict.
First three keys (translation, type, pronunciation) are obligatory
"""

english_polish_dictionary = {'abbreviation': {'translation': 'skrót, cos', 'type': 'noun', 'pronunciation': '[əˌbri:viˈeɪʃən]',
                                              'additional': 'skrót (wyrazu lub wyrażenia) \nplural: abbreviations' }}

print(english_polish_dictionary['abbreviation']['type'])

for key, value in english_polish_dictionary.items():
    print(key)
    print(value)
    for value in english_polish_dictionary[key].values():
        print(value)