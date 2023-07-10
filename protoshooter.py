import pygame
from classprotoshooter import *
import random

#Initialize
pygame.init()
screen = setDisplay()
setClock()

#Initialize Player
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25) 

#Start Music
pygame.mixer.init()
pygame.mixer.music.load('Music' + '/Komiku.mp3')
pygame.mixer.music.play(-1)

#Game Loop
run = True
while run:

    #Player Move
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.moveLeft()
    elif key[pygame.K_d] == True:
        player.moveRight()
    elif key[pygame.K_w] == True:
        player.moveUp()
    elif key[pygame.K_s] == True:
        player.moveDown()

    #Event Handler
    for event in pygame.event.get():

        #Quit Game
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        #Shoot
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Shot.")
                shot = Bullet(player.avatar.x, player.avatar.y, 10, 10)
                while (shot.bullet.y) > -SCREEN_HEIGHT:
                    shot.update()
                    shot.draw(screen)

    update(screen, player)
    screen.fill((0,0,0))
pygame.quit()