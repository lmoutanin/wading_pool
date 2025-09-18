import pygame
from pygame import QUIT

pygame.init()

image = pygame.image.load("x.jpg")
ecran = pygame.display.set_mode((1000, 600))

continuer = True


def drawStickman():
    center_x = 600 // 2
    center_y = 600 // 2
    pygame.draw.circle(ecran, (255, 255, 255), (center_x, center_y - 100), 50, 2)
    # Body
    pygame.draw.line(ecran, "WHITE", (center_x, center_y - 50), (center_x, center_y + 150), 3)
    # Arms
    pygame.draw.line(ecran, "WHITE", (center_x, center_y), (center_x - 100, center_y + 50), 3)
    pygame.draw.line(ecran, "WHITE", (center_x, center_y), (center_x + 100, center_y + 50), 3)
    # Legs
    pygame.draw.line(ecran, "WHITE", (center_x, center_y + 150), (center_x - 80, center_y + 300), 3)
    pygame.draw.line(ecran, "WHITE", (center_x, center_y + 150), (center_x + 80, center_y + 300), 3)


while continuer:
    ecran.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    drawStickman()
    pygame.display.flip()

pygame.quit()
