from random import choice

class RandomWalk():
    """The class designed to generate a random walk"""

    def __init__(self, num_points=5000):
        """Initialization of random walk attributes"""
        self.num_points = num_points

        """Initial point has coordinates (0, 0)"""
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generating all points for a random walk"""

        # Using the steps until the expected number of points is reached
        while len(self.x_values) < self.num_points:

            # Determining the direction and distance to be covered in a given direction
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejecting moves that lead nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Setting next x and y values:
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Determining the direction and distance to be covered in a given direction"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

