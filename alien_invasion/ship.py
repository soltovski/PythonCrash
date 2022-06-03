import pygame

class Ship:
    '''Classe que gerencia a nave'''

    def __init__(self, ai_game):
        '''Inicializa a nave e seta sua posição inicial'''
        self.screen = ai_game.screen #
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #carrega a imagem da nave e captura seu rect
        self.image = pygame.image.load('images/ship.bmp') #carrega a imagem
        self.rect = self.image.get_rect() #captura o rect

        #começa cada nova nave no fundo central da tela
        self.rect.midbottom = self.screen_rect.midbottom

        #armazena um valor decimal para a posicao horizontal da nave
        self.x = float(self.rect.x)

        #flag movimentação
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''atualiza a posicao da nave, baseada na movimentação da flag'''
        #atualiza a posicao x da nave, do rect não
        if self.moving_right and self.rect.right < self.screen_rect.right:#limita borda dir
            self.x += self.settings.ship_speed #se continuar pressionada
        if self.moving_left and self.rect.left > 0: #limita borda esquerda
            self.x -= self.settings.ship_speed

        #atualiza o objeto rect
        self.rect.x = self.x

    def blitme(self):
        '''Faz surgir na tela a nave, na posição indicada'''
        self.screen.blit(self.image, self.rect)


















'''import pygame

class Ship():
    def __init__(self, screen):
        #Inicializa a nave e a posiciona
        self.screen = screen
        #Carrega a imagem da nave e a trata como retângulo
        self.image = pygame.image.load('images/ship.bmp') # carrega imagem da nave
        self.rect = self.image.get_rect() #atribui o rect da imagem à rect
        self.screen_rect = screen.get_rect() #atribui o rect da screen à screen_rect

        #começa cada nova nave pela parte CENTRAL de BAIXO da tela
        self.rect.centerx = self.screen_rect.centerx # posição x da nave == posição x da tela
        self.rect.bottom = self.screen_rect.bottom   #         y         ==         y

    def blitme(self):
        #Faz APARECER a nave na sua posição self.rect
        self.screen.blit(self.image, self.rect)'''