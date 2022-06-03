import pygame

class Carro:
    '''Classe que gerencia os carros'''

    def __init__(self, def_jogo):
        '''inicializa o carro na posiçao indicada'''
        self.tela = def_jogo.tela#var local tela recebe o atributo tela passado por parâmetro
        self.tela_rect = def_jogo.tela.get_rect()#
        self.config = def_jogo.config

        #carrega a imagem da nave e pega seu rect
        self.imagem = pygame.image.load('imagens/carro_driver.bmp')
        self.rect = self.imagem.get_rect() #rect da imagem

        #começa a imagem do carro na posição central inferior da tela
        self.rect.midbottom = self.tela_rect.midbottom

        #guarda o valor decimal da posicao horiontal do carro
        self.x = float(self.rect.x)

        #flag de movimentação
        self.flag_mov_direita = False
        self.flag_mov_esquerda = False

    def att_pos_carro(self):
        '''Atualiza a posicao do carro, baseada na flag de movimentação'''
        #atualiza o valor de x do carro, não do rect:
        #se a tecla direit está presionada E a posição x+ do carro não encontrou com a borda direita
        if self.flag_mov_direita and self.rect.right < self.tela_rect.right:
            self.x += self.config.carro_veloc
        elif self.flag_mov_esquerda and self.rect.left > 0:#se a tecla esquerda está pressionada E a posição x- do
            self.x -= self.config.carro_veloc               #carro ainda não encontrou a borda esquerda

        #atualiza do rect objeto de self.x
        self.rect.x = self.x


    def blitme(self):
        '''Faz surgir a imagem do carro na tela'''
        self.tela.blit(self.imagem, self.rect)