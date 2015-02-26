import pygame
from pygame.locals import *
from classes import block

def create() :
    maMap = pygame.sprite.RenderClear()
    for k in range(4) :
        for i in range(22) :
            for j in range(10):
                rect = [j*16+k*180 +50 ,i*16+150]
                maMap.add(block.Block(rect))
    return maMap
