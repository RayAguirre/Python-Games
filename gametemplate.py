from deckofcards import *
import pygame
import random

#Initialize Pygame
pygame.init()

#Set Screen Display
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Set Game Clock
clock = pygame.time.Clock()
fps = 60

#Start Music
pygame.mixer.init()
pygame.mixer.music.load('Music' + '/Komiku.mp3')
pygame.mixer.music.play(-1)

#Game Loop
run = True
while run:

    #Event Handler
    for event in pygame.event.get():
        #Quit Game
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    pygame.display.update()
    screen.fill((0,0,0))
pygame.quit()