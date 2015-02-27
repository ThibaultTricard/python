import pygame
from pygame.locals import *
from classes import block

def create() :
    maMap = pygame.sprite.RenderClear()
    for k in range(4) :
        for i in range(22) :
            for j in range(10):
                rect = [j*16+k*180 +50 ,i*16+150]
                maMap.add(block.Block(rect,0))
    return maMap

def update(forms,groupeForm,groupeFormStockee) :
    print "test1"
    maMap = pygame.sprite.RenderClear()
    for k in range(4) :
        for i in range(22) :
            for j in range(10):
                x=j*16+k*180 +50
                y=i*16+150
                caseOccupe=False
                for sprite in groupeForm.sprites():
                    if sprite.rect.x==x and sprite.rect.y==y:
                        caseOccupe=True
                        maMap.add(sprite)
                if caseOccupe==False:
                    maMap.add(block.Block([x,y],0))

    return maMap

def creer(form, joueur):
    print form.form[form.formActuelle]
    maForm = pygame.sprite.RenderClear()
    for i in range(len(form.form[form.formActuelle])):
        for j in range(len(form.form[form.formActuelle][i])):
            if form.form[form.formActuelle][i][j] >=1 :
                rect = [(j+form.pos1[1])*16+joueur*180 +50 ,(i+form.pos1[0])*16+150]
                maForm.add(block.Block(rect,form.form[form.formActuelle][i][j]))
    return maForm
