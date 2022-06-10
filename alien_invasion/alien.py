import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Classe que representa um único alien no esquadrão'''

    def __init__(self, ai_game):
        '''Inicializa o alien e define sua posição inicial'''
        super().__init__()
        self.screen =ai_game.screen
        self.settings = ai_game.settings

        #carrega a imagem do alien e define seu atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #comeca cada novo alien perto da parte superior esquerda da tela
        self.rect.x = self.rect.width # inicia a uma distância dele mesmo em relação a x
        self.rect.y = self.rect.height # inicia a uma distância dele mesmo em relação a y

        #armazena a posicao horintal exata do alien
        self.x = float(self.rect.x)

    def update(self):
        '''Move o alien para direita'''
        self.x += self.settings.alien_speed
        self.rect.x = self.x

