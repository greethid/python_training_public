"""This file contains english-polish dictionary, english words as keys of dict.
First three keys (translation, type, pronunciation) are obligatory
"""

english_polish_dictionary = {
    'a': {'translation': 'jakiś, niejaki, jeden, na, w, za',
          'type': 'PRZEDIM [przed rzecz. policz.]',
          'pronunciation': '[eɪ] akcentowane, [ə] nieakcentowane',
          'additional': 'jakiś [najczęściej nie tłumaczone na j. polski], niejaki [przed nazwiskami,imionami],'
                        ' jeden [czasem pomijane w tłumaczeniu], na [przy określaniu częstotliwości], w [przy określaniu częstotliwości],'
                        ' za [przy określaniu cen], A - ocena celująca/bardzo dobra [najwyższa ocena w szkole brytyjskiej]'},
    'abbreviation': {'translation': 'skrót',
                     'type': 'RZ', 'pronunciation': '[əˌbri:viˈeɪʃən]',
                     'additional': 'skrót (wyrazu lub wyrażenia)'},
                             }

print(english_polish_dictionary['abbreviation']['type'])

for key, value in english_polish_dictionary.items():
    print(key)
    print(value)
    for value in english_polish_dictionary[key].values():
        print(value)

print(english_polish_dictionary['a']['additional'])
tab = english_polish_dictionary['a']['additional'].split(', ')
for info in tab:
    print(info)