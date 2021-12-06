with open('three_rings.txt', 'r') as text:
    all_file = text.read()

    without_dots = all_file.replace('.', '')
    without_comas = without_dots.replace(',', '')
    same_case = without_comas.upper()
    words = same_case.split()
    set_ready = set(words)

    print(set_ready)
    print(type(set_ready))
