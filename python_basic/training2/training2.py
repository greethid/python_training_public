# Take file "three_rings.txt" and build file "three_wings.txt".
# (by exchanging any Ring into Wing).

with open('three_rings.txt', 'r') as text:
    all_file = text.read().replace('Ring', 'Wing').replace('ring', 'wing')
    # words = all_file.split()

    print(all_file)

    with open('three_wings.txt', 'w') as text2:
        text2.write(all_file)
