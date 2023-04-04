import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Creating a new random walk until end of the loop
while True:
    # Preparing random walk data and displaying points
    rw = RandomWalk()
    rw.fill_walk()

    # Displaying random walk points
    plt.style.use('classic')
    fix, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    # Highlighting the first and the last random walk points
    ax.scatter(0, 0, c='green', edgecolor='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=50)
    plt.show()

    keep_running = input("Do you want to create a new random walk? (y/n): ")
    if keep_running == 'n':
        break