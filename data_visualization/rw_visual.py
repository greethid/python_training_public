import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Creating a new random walk until end of the loop
while True:
    # Preparing random walk data and displaying points
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Displaying random walk points
    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(16, 10), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    # ax.plot(rw.x_values, rw.y_values, linewidth=3)
    # Highlighting the first and the last random walk points
    ax.scatter(0, 0, c='green', edgecolor='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=50)

    # Hiding axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Do you want to create a new random walk? (y/n): ")
    if keep_running == 'n':
        break