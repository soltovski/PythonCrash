import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Classe que gerencia os tiros dados pela nave'''

    def __init__(self, parametro): #parametro se refere ao objeto associado ao __main__ de nave_jogo.
     '''Cria um objeto bala, saindo da posição atual da nave'''
     super().__init__()  #dá acesso aos métodos e propriedade de Sprite
     self.tela = parametro.tela
     self.settings =parametro.settings
     self.cor = self.settings.bullet_cor

     #cria uma bala rect em (0,0) e então ajusta sua posição em função da posição de ship
     self.bullet_rect = pygame.Rect(0,0, self.settings.bullet_lar,
                                    self.settings.bullet_alt)
     self.bullet_rect.midtop = parametro.ship.ship_rect.midtop

     #armazena a posição da bala como decimal
     self.pos_y = float(self.bullet_rect.y)

    def update(self):
         '''move a bala para cima na tela'''
         #atualiza a posição decimal da bala
         self.pos_y -= self.settings.bullet_veloc
         #atualiza a posição rect da bala
         self.bullet_rect.y = self.pos_y

    def desenha_bullet(self):
        '''desenha a bala na tela'''
        pygame.draw.rect(self.tela, self.cor, self.bullet_rect)