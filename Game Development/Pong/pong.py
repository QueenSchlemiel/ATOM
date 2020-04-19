# https://www.101computing.net/pong-tutorial-using-pygame-adding-the-paddles/

# Import pygame and initialize game
import pygame
from paddle import Paddle
pygame.init()

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# define the paddles
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# List of sprites in game
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the List
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

playGame = True

# used to control how fast the screen updates
clock = pygame.time.Clock()

# Main program loop
while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playGame = False

    # Game logic
    all_sprites_list.update()

    # clear screen to BLACK
    screen.fill(BLACK)
    # Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # Draw the paddles
    all_sprites_list.Draw(screen)

    pygame.display.flip()
    # Frame rate is 60 frames per second
    clock.tick(60)

pygame.quit()
