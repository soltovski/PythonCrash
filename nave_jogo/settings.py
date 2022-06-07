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

        #preferencias de munição
        self.bullet_veloc = 0.6
        self.bullet_lar = 3
        self.bullet_alt = 15
        self.bullet_cor = (60,60,60)
        self.bullet_permit = 3
