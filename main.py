import pygame
import shape
import colors
import sys


pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drawing Application")

white = (255,255,255)
container = []
drawing = False
running = True
number = ''


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                #mousePos = event.pos
                #container.append(mousePos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                print(container)
                container.clear()
                screen.fill(colors.BLACK)
            if event.unicode.isdigit():
                number = int(event.unicode)

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if(number == ''):
            test = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(mouse_pos[0], mouse_pos[1], 10, 10))
        else:
            test = pygame.draw.rect(screen, colors.colorWheel[number], pygame.Rect(mouse_pos[0], mouse_pos[1], 10, 10))


    pygame.display.flip()

pygame.quit()
sys.exit()