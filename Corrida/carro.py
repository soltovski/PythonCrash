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
        self.mov_direita = False
        self.mov_esquerda = False

    def att_pos_carro(self):
        '''Atualiza a posicao do carro, baseada na flag de movimentação'''
        #atualiza o valor de x do carro, não do rect
        if self.mov_direita:
            self.x += self.config.carro_veloc
        elif self.mov_esquerda:
            self.x -= self.config.carro_veloc

        #atualiza do rect objeto de self.x
        self.rect.x = self.x


    def blitme(self):
        '''Faz surgir a imagem do carro na tela'''
        self.tela.blit(self.imagem, self.rect)