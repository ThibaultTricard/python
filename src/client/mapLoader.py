#!/usr/bin/env python
# coding: utf-8
class MapLoader() :

    def __init__(self) :
        pass

    def load(self,List) :
        maMap = {0:''}
        caracter_sprite = pygame.sprite.RenderClear()
        wall_sprite = pygame.sprite.RenderClear()
        for i in range(len(List)) :
            for j in range(len(List[i])):

                if List[i][j] == 1 :
                    rect = [j*16,i*16]
                    #ajouter block de couleur

                if List[i][j] == 2 :
                    rect = [j*16,i*16]
                    #ajouter block de couleur

                if List[i][j] == 3 :
                    rect = [j*16,i*16]
                    #ajouter block de couleur

                if List[i][j] == 4 :
                    rect = [j*16,i*16]
                    #ajouter block de couleur

                if List[i][j] == 5 :
                    rect = [j*16,i*16]
                    #ajouter block de couleur

                if List[i][j] == 6 :
                    rect = [j*16,i*16]
                    #ajouter block de couleur

                if List[i][j] == 6 :
                    rect = [j*16,i*16]
                    #ajouter block de couleur

        maMap[1] = wall_sprite
        maMap[2] = caracter_sprite
        return maMap
