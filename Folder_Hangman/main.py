"""
    Clément BADRONE
    Last Update 18/09/2024
    Epitech Pre-Pool PreMSC
"""

import pygame

"""Inside your main.py, create a function that draws a stickman inside the game window."""

pygame.init()
screen = pygame.display.set_mode((600,600))
background = pygame.image.load(".\Folder_Hangman\\background.jpg")
pygame.display.set_caption("Hangman")

BLACK = (0, 0, 0)

def draw_stickman(screen, x, y):
    pygame.draw.circle(screen, BLACK, (x, y), 30, 2)
    
    pygame.draw.line(screen, BLACK, (x, y + 30), (x, y + 120), 2)
    
    pygame.draw.line(screen, BLACK, (x - 50, y + 60), (x + 50, y + 60), 2)
    
    pygame.draw.line(screen, BLACK, (x, y + 120), (x - 40, y + 180), 2)
    pygame.draw.line(screen, BLACK, (x, y + 120), (x + 40, y + 180), 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))
    draw_stickman(screen, 600 // 2, 600 // 4)
    pygame.display.flip()

pygame.quit()