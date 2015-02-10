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
                    wall_sprite.add(WallBloc(rect))

                if List[i][j] == 2 :
                    rect = [j*16,i*16]
                    caracter_sprite.add(Caracter(rect))

        maMap[1] = wall_sprite
        maMap[2] = caracter_sprite
        return maMap
