#!/usr/bin/env python
# coding: utf-8
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

"""
Ecrit le message d'attente des joueurs
"""
def ecrireMessageAcceuil():
    font=pygame.font.SysFont("broadway",36,bold=False,italic=False)
    text=font.render("En attente d'autres joueurs",1,(200,200,250))
    return text

"""
Ecrit le message de find de partie aux joueurs
"""
def ecrireMessageFin(gagnant):
    font=pygame.font.SysFont("broadway",28,bold=False,italic=False)
    if gagnant!="":
        text=font.render("Joueur "+gagnant+" est le gagnant",1,(200,200,250))
    else:
        text=font.render("Fin du jeu ! Attendre la fin des autres joueurs",1,(200,200,250))

    return text
