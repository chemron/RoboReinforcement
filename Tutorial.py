import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAY_SURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")

# colours:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

DISPLAY_SURF.fill(white)

pygame.draw.polygon(DISPLAY_SURF, green,
                    ((0, 250), (500, 250), (500, 400), (0, 400))
                    )
pygame.draw.rect(DISPLAY_SURF, red, (200, 150, 100, 100))
pygame.draw.polygon(DISPLAY_SURF, black,
                    ((200, 150), (250, 100), (300, 150)))
pygame.draw.circle(DISPLAY_SURF, blue, (225, 200), 15)
pygame.draw.circle(DISPLAY_SURF, blue, (275, 200), 15)
pygame.draw.rect(DISPLAY_SURF, white, (240, 200, 20, 50))

pixObj = pygame.PixelArray(DISPLAY_SURF)
pixObj[257][217] = black
del pixObj

# Game loop
while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
