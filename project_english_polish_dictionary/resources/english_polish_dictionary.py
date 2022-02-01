"""This file contains english-polish dictionary, english words as keys of dict."""


#english_polish_dictionary
eng_pol_dict = {
    'a': ('jakiś', 'niejaki', 'jeden', 'na', 'w', 'za'),
    'A-1': ('znakomity', 'doskonały'),
    'abaci': ('liczydła',),
    'aback': ('wstecz',),
    'to be taken aback': ('być wytrąconym z równowagi',),
    'abacus': ('liczydło',),
    'abandon': ('porzucać', 'opuszczać', 'zarzucać', 'zaniechać', 'porzucać', 'zrezygnować', 'żywiołowość'),
    'abandoned': ('opuszczony', 'opustoszały', 'nieużywany', 'porzucony', 'zostawiony', 'żywiołowy', 'niekontrolowany'),
    'abandoned behaviour': ('niekontrolowane zachowanie',),
    'abandonment': ('opuszczenie', 'porzucenie', 'zaniechanie', 'zrezygnowanie'),
    'abase': ('poniżyć', 'obniżyć'),
    'to abase oneself': ('upokorzyć się',),
    'abasement': ('upokorzenie', 'poniżenie'),
    'abash': ('zawstydzić', 'zmieszać', 'zbić z tropu'),
    'abashed': ('speszony', 'zawstydzony'),
    'abashment': ('zmieszanie', 'zakłopotanie'),
    'abate': ('zmniejszyć', 'osłabnąć', 'uciszyć', 'obniżyć'),
    'abate a nuisance': ('uciszyć hałas',),
    'abatement': ('zmniejszenie', 'osłabnięcie', 'uciszenie się', 'spadek', 'obniżka'),
    'tax abatement': ('ulga podatkowa',),
    'abbacy': ('urząd opata',),
    'abbess': ('ksieni', 'matka przełożona'),
    'abbey': ('opactwo',),
    'abbot': ('opat',),
    'abbreviate': ('skracać',),
    'abbreviation': ('skrót',),
    'ABC': ('alfabet', 'podstawy'),
    'abdicate': ('abdykować', 'zrzekać się'),
    'abdication': ('abdykacja', 'zrzeczenie się'),
    'abdomen': ('brzuch', 'odwłok'),
    'abdominal': ('brzuszny', 'odwłokowy'),
    'abduct': ('porwać', 'uprowadzić'),
    'abduction': ('porwanie', 'uprowadzenie'),
    'abductor': ('porywacz', 'sprawca uprowadzenia'),
    'aberrance': ('anormalność', 'odchylenie od normy'),
    'aberrant': ('zboczony', 'błędny', 'anormalny', 'odchylony od normy'),
    'aberration': ('odchylenie', 'zboczenie', 'anormalność', 'odchylenie od normy'),
    'mental aberration': ('zaburzenie umysłowe',),
    'abet': ('nakłaniać do przestępstwa', 'podżegać'),
    'abetment': ('podżeganie do przestępstwa',),
    'abeyance': ('stan zawieszenia',),
    'abhor': ('czuć odrazę', 'czuć wstręt'),
    'abhorrence': ('odraza', 'wstręt', 'rzecz budząca odrazę'),
    'abhorrent': ('wstrętny', 'odrażający'),
    'abidance': ('przestrzeganie', 'dotrzymywanie'),
    'abide': ('znosić', 'przestrzegać', 'dotrzymywać'),
    'can\'t abide sb/sth': ('nie znosić kogoś/czegoś', 'nie cierpieć kogoś/czegoś'),
    'abide by sth': ('dotrzymywać czegoś', 'przestrzegać czegoś'),
    'abiding': ('trwały', 'stały'),
    'ability': ('zdolność', 'umiejętność'),
    'abilities': ('zdolności', 'umiejętności'),
    'ability to do sth': ('zdolność do czegoś', 'zdolność robienia czegoś'),
    'do sth to the best of sb\'s ability': ('zrobić coś jak najlepiej', 'zrobić coś możliwie jak najlepiej'),
    'abject': ('nikczemny', 'podły'),
    'abjection': ('nędza', 'upodlenie'),
    'abjectly': ('nędznie', 'nikczemnie', 'podle'),
    'ablative': ('narzędnik',),
    'ablaze': ('w ogniu', 'w płomieniach', 'płonący', 'palący się'),
    'able': ('zdolny', 'pojętny'),
    'be able to do sth': ('potrafić', 'umieć', 'móc', 'być w stanie', 'zdołać'),
    'able-bodied': ('krzepki', 'silny'),
    'abloom': ('w kwiatach', 'w rozkwicie'),
    'abnormal': ('anormalny', 'nieprawidłowy'),
    'abnormality': ('anormalność', 'nieprawidłowość'),
    'abnormally': ('anormalnie', 'nieprawidłowo'),
    'aboard': ('na pokładzie', 'na pokład'),
    'all aboard': ('wszyscy na pokład',),
    'abode': ('znosić', 'przestrzegać', 'dotrzymywać'),
    'abolish': ('obalać', 'znosić'),
    'abolishment': ('zlikwidowanie', 'zniesienie'),
    'abolition': ('zniesienie', 'obalenie'),
    'abolitionism': ('abolicjonizm',),
    'abolitionist': ('zwolennik zniesienia niewolnictwa',),
    'abominable': ('obrzydliwy', 'wstrętny', 'ohydny'),
    'abominate': ('czuć odrazę', 'nienawidzić'),
    'abomination': ('wstręt', 'odraza', 'obrzydliwość', 'paskudztwo'),
    'aboriginal': ('tubylczy', 'rdzenny'),
    'Aborigine': ('aborygen', 'tubylec'),
    'Aboriginal tribes': ('tubylcze szczepy',),
    'abort': ('poronić', 'przerywać ciążę'),
    'abortion': ('aborcja', 'zabieg przerwania ciąży'),
    'abortionist': ('osoba przeprowadzająca aborcję',)

    }

if __name__ == '__main__':
    for key, value in eng_pol_dict.items():
        print(key + ': ', end='')
        print(value)
        if type(value) != tuple:
            raise ValueError(f'Value for key {key} is not a tuple!')
            break

    print(len(eng_pol_dict))
    print('OK')


