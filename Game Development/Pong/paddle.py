import pygame
BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    def _init_(self, color, width, height):
        # call the parent class to create the Sprite
        super()._init_()

        # Pass color of paddle and x,y position with height and width
        # set background color to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle - rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the object
        self.rect = self.image.get_rect()
