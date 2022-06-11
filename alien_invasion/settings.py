class Settings:
    '''classe para gerenciar todas as preferencias do jogo'''

    def __init__(self):
        """inicializa as preferencias do jogo"""
        #preferências de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #preferencias da nave
        self.ship_speed = 1.5

        #preferÊncias das munições
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #preferências de aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #fleet_direction 1 representa 'direita'; -1 'esquerda
        self.fleet_direction = 1



