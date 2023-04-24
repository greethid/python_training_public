from die import Die

from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two dice of type D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Perform a certain number of die throws and put results on the list
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Results analysis
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range (3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Data visualisation
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency'}
my_layout = Layout(title='Results of rolling three dice D6 10000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')