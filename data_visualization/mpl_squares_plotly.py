import matplotlib.pyplot as plt

from plotly.graph_objs import Bar, Layout
from plotly import offline

x_values = range(1, 1001)
y_values = [x**3 for x in x_values]
squares2 = [x**2 for x in range(-100, 100)]

x_values2 = list(range(1, 1001))
y_values2 = list(range(1, 1001))

plt.style.use('ggplot')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.plot(x_values, y_values, linewidth=3)

# Defining the chart title and axis labels
ax.set_title('Square of numbers', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Squared values', fontsize=14)

# Defining the size of the labels
ax.tick_params(axis='both', labelsize=14)

# Defining the range for each axis
ax.axis([0, 1100, 0, 1100000])

# plt.show()

# Save to a file
# plt.savefig('squares_plot.png', bbox_inches='tight')

# fig, ax = plt.subplots()
# ax.plot(squares2)
# plt.show()

#----------------------------------------------------------
# Second approach with plotly library

# data = [Bar(x=x_values2, y=y_values2)]
data = [Bar(x=x_values2, y=squares2)]
x_axis_config = {'title': 'Values'}
y_axis_config = {'title': 'Squared values'}
my_layout = Layout(title='Square of numbers',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='squares.html')