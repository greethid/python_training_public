import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
squares2 = [x**2 for x in range(-100, 100)]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Defining the chart title and axis labels
ax.set_title('Square of numbers', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Squared values', fontsize=14)

# Defining the size of the labels
ax.tick_params(axis='both', labelsize=14)

plt.show()

# fig, ax = plt.subplots()
# ax.plot(squares2)
# plt.show()