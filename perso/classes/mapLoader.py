import pygame
from pygame.locals import *
from classes import block

#on crée les plateaux de jeux
def create() :
    maMap = pygame.sprite.RenderClear()
    for k in range(4) :
        for i in range(22) :
            for j in range(10):
                rect = [j*16+k*180 +50 ,i*16+150]
                maMap.add(block.Block(rect,0))
    return maMap

#on crée un groupe de sprite sur la map d'un joueur
def paint(form, joueur):
    #on crée le groupe de sprite
    maForm = pygame.sprite.RenderClear()
    #on remplit le groupe grâce aux informations pasées dans la forme
    for i in range(len(form.form[form.formActuelle])):
        for j in range(len(form.form[form.formActuelle][i])):
            if form.form[form.formActuelle][i][j] >=1 :
                rect = [(j+form.pos1[1])*16+joueur*180 +50 ,(i+form.pos1[0])*16+150]
                maForm.add(block.Block(rect,form.form[form.formActuelle][i][j]))
    return maForm

"""
Ecrit le score sous le plateau des joueurs
"""
def ecrireScore(pseudo,score):
    font=pygame.font.SysFont("broadway",24,bold=False,italic=False)
    text=font.render(pseudo+":"+str(score),1,(255,255,255))
    return text
