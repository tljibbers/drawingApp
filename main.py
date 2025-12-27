import pygame
import shape
import colors
import sys


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drawing Application")

white = (255,255,255)
container = []


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousePos = event.pos
                container.append(mousePos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                container.clear()

    screen.fill(white)

    for x,y in container:
        test = shape.Rectangle(5, 5, colors.BLUE)
        test.draw(screen, x, y)
    pygame.display.flip()

pygame.quit()
sys.exit()