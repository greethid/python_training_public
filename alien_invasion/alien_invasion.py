import sys
import pygame

class AlienInvasion:
    "General class dedicated to managing the resources and the way the game works."

    def __init__(self):
        "Initialize game and create resources."

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        #Define the background color
        self.bg_color = (250, 230, 230)

    def run_game(self):
        "Start main loop of the program"

        while True:
            #Waiting for input from a user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Refresh screen after each iteration of the loop
            self.screen.fill(self.bg_color)

            #Displaying the last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    #Creating a copy of the game and launching it
    ai = AlienInvasion()
    ai.run_game()


