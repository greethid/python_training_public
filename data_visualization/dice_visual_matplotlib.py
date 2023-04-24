from die import Die

from plotly.graph_objs import Bar, Layout
from plotly import offline

import matplotlib.pyplot as plt

# Create two dice of type D6
die_1 = Die()
die_2 = Die()

# Perform a certain number of die throws and put results on the list
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Results analysis
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Data visualisation
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency'}
my_layout = Layout(title='Results of rolling two dice D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

#------------------------------------------------------------------------------
# Second approach with matplotlib instead of plotly library

plt.style.use('classic')
fix, ax = plt.subplots()
ax.scatter(x_values, frequencies, s=15)
# ax.plot(x_values, frequencies, linewidth=3)

plt.show()
