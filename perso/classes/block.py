import pygame
from pygame.locals import *

class Block(pygame.sprite.Sprite):

    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/empty.png')
        self.image = pygame.transform.scale(self.image, (int(16), int(16)))
        self.rect = self.image.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.speed = [0,0]

    def changerImage(self,color):
        self.image = pygame.image.load('image/'+color+'.png')
        self.image = pygame.transform.scale(self.image, (int(16), int(16)))
