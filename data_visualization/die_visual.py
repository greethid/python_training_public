from die import Die

from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a die of type D6
die = Die()

# Perform a certain number of die throws and put results on the list
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

# Results analysis
frequencies = []
for value in range (1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Data visualisation
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency'}
my_layout = Layout(title='Results of rolling a single die D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')