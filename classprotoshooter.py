import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

def setDisplay():
    #Set Screen Dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def setClock():
    #Set Up Clock
    clock = pygame.time.Clock()
    target_fps = 10  # Desired frames per second

def update(screen, player):
    pygame.draw.rect(screen, (255, 0, 0), player.avatar)
    pygame.display.update()

class Player:
    def __init__(self, x, y, w, h):
        self.location = (x, y)
        self.hitbox = (w, h)
        self.movement_speed = 1
        self.avatar = pygame.Rect(x, y, w, h)

    def moveLeft(self):
        self.avatar = self.avatar.move(-1 * self.movement_speed, 0)
    def moveRight(self):
        self.avatar = self.avatar.move(1 * self.movement_speed, 0)
    def moveUp(self):
        self.avatar = self.avatar.move(0, -1 * self.movement_speed)
    def moveDown(self):
        self.avatar = self.avatar.move(0, 1 * self.movement_speed)

class Bullet:
    def __init__(self, x, y, w, h):
        self.location = (x, y)
        self.hitbox = (w, h)
        self.movement_speed = 10
        self.bullet = pygame.Rect(x, y, w, h)

    def update(self):
        self.bullet = self.bullet.move(0, -1 * self.movement_speed)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), 
                            (self.bullet.x, self.bullet.y), 10)

print("Successfully Imported")