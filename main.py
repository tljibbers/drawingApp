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
history = []
eraseHistory = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                historyCopy = []
                historyCopy = history.copy()
                container.append(historyCopy)
                last_segment = container.pop()
                history.clear()
                print(container)
                print(last_segment)

        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                print(container)
                container.clear()
                screen.fill(colors.BLACK)
            if event.unicode.isdigit():
                number = int(event.unicode)
            if event.key == pygame.K_z and pygame.key.get_mods() and pygame.KMOD_CTRL:
                eraseHistory = True

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if(number == ''):
            test = pygame.draw.rect(screen, colors.BLUE, pygame.Rect(mouse_pos[0], mouse_pos[1], 10, 10))
            history.append(mouse_pos)
        else:
            test = pygame.draw.rect(screen, colors.colorWheel[number], pygame.Rect(mouse_pos[0], mouse_pos[1], 10, 10))
            history.append(mouse_pos)

    if eraseHistory:
        for x, y in last_segment:
            pygame.draw.rect(screen, colors.BLACK, pygame.Rect(x, y, 10, 10))
        eraseHistory = False


    pygame.display.flip()

pygame.quit()
sys.exit()