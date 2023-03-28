import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**3 for x in x_values]
squares2 = [x**2 for x in range(-100, 100)]

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

plt.show()

# Save to a file
# plt.savefig('squares_plot.png', bbox_inches='tight')

# fig, ax = plt.subplots()
# ax.plot(squares2)
# plt.show()