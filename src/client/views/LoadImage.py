#!/usr/bin/env python
# coding: utf-8
import pygame
import os

class LoadImage:
    def __init__(self,cheminImage):
        self.cheminImage=cheminImage
          
    def load_png(self,name):
        """Load image and return image object"""
        fullname=os.path.join('.',name)
        try:
            image=pygame.image.load(fullname)
            if image.get_alpha is None:
                image=image.convert()
            else:
                image=image.convert_alpha()
        except pygame.error, message:
            print 'Cannot load image:', fullname
            raise SystemExit, message
        return image,image.get_rect()
    
    def getImagePng(self):
        image,rect=self.load_png(self.cheminImage)
        return image,rect
    
        
        