import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Classe que gerencia as balas disparadas pela nave'''

    def __init__(self, ai_game):
        """cria um objeto bala, na posição atual da nave"""
        super().__init__()#para funcionar com o Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #cria uma bala rect em (0,0) e então seta a posição correta
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #armazena a posição da bala em valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """move a bala para cima na tela"""
        #atualiza a posição decimal da bala
        self.y -= self.settings.bullet_speed
        #atualiza a posição rect
        self.rect.y = self.y

    def draw_bullet(self):
        """desenha a bala na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)