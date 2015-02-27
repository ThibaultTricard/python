import pygame
from pygame.locals import *

class Block(pygame.sprite.Sprite):

    def __init__(self, rect, num):
        pygame.sprite.Sprite.__init__(self)
        if num == 0:
            self.image = pygame.image.load('image/empty.png')
        if num == 1 :
            self.image = pygame.image.load('image/vert.png')
        if num == 2 :
            self.image = pygame.image.load('image/bleuFonce.png')
        if num == 3 :
            self.image = pygame.image.load('image/orange.png')
        if num == 4 :
            self.image = pygame.image.load('image/jaune.png')
        if num == 5 :
            self.image = pygame.image.load('image/bleuClaire.png')
        if num == 6 :
            self.image = pygame.image.load('image/rouge.png')
        if num == 7 :
            self.image = pygame.image.load('image/violet.png')
        self.image = pygame.transform.scale(self.image, (int(16), int(16)))
        self.rect = self.image.get_rect()
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.speed = [0,0]

    def changerImage(self,color):
        self.image = pygame.image.load('image/'+color+'.png')
        self.image = pygame.transform.scale(self.image, (int(16), int(16)))
