import random
import plotly.express as px

# symulacja rzutu kością
def roll_dice():
    return random.randint(1, 6)

# liczba rzutów kością
num_rolls = 1000

# lista wyników rzutów
rolls = [roll_dice() for i in range(num_rolls)]

# tworzenie histogramu wyników
fig = px.histogram(rolls, nbins=6, labels={'value': 'Wynik', 'count': 'Liczba rzutów'})

# wyświetlenie wykresu
fig.show()