import  pygame.font

class Button():

    def __init__(self, ai_game, screen, msg):
        """Initialization of a button's attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Define dimensions and properties of a button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create a rectangle of a button and centre it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Text displayed on button has to be prepared only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Place a text on the generated screen and center a text on a button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Display an empty button and then text on it
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

