import pygame
import pygame.locals as loc
import sys

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAY_SURF = pygame.display.set_mode((1200, 600), 0, 32)
pygame.display.set_caption("Animation")


white = (255, 255, 255)

sandwich_img = pygame.image.load('resources/sandwich.png')
sandwich_img = pygame.transform.scale(sandwich_img, (164, 100))

sandwich_x = 20
sandwich_dx = 10
sandwich_y = 10
sandwich_dy = 10

print(sandwich_img.get_width())

while True:
    DISPLAY_SURF.fill(white)

    if (sandwich_x >= 1200 - sandwich_img.get_width()
            or sandwich_x <= 0):
        sandwich_dx = -sandwich_dx
    if (sandwich_y >= 600 - sandwich_img.get_height()
            or sandwich_y <= 0):
        sandwich_dy = -sandwich_dy

    sandwich_x += sandwich_dx
    sandwich_y += sandwich_dy

    DISPLAY_SURF.blit(sandwich_img, (sandwich_x, sandwich_y))

    for event in pygame.event.get():
        if event == loc.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
