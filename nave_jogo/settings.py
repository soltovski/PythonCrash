class Settings:
    '''Classe para preferencias do jogo'''

    def __init__(self):
        '''Inicializa as preferencias do jogo'''
        #preferencias de tela
        self.tela_lar = 600
        self.tela_alt = 400
        self.tela_cor = (230,230,230)

        #preferências da nave
        self.veloc_ship = 0.8