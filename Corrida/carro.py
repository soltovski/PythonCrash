import pygame

class Carro:
    '''Classe que gerencia os carros'''

    def __init__(self, def_jogo):
        '''inicializa o carro na posiçao indicada'''
        self.tela = def_jogo.tela#var local tela recebe o atributo tela passado por parâmetro
        self.tela_rect = def_jogo.tela.get_rect()#

        #carrega a imagem da nave e pega seu rect
        self.imagem = pygame.image.load('imagens/carro_driver.bmp')
        self.rect = self.imagem.get_rect() #rect da imagem

        #começa a imagem do carro na posição central inferior da tela
        self.rect.midbottom = self.tela_rect.midbottom

        #flag de movimentação
        self.mov_direita = False

    def att_pos_carro(self):
        '''Atualiza a posicao do carro, baseada na flag de movimentação'''
        if self.mov_direita:
            self.rect.x += 1


    def blitme(self):
        '''Faz surgir a imagem do carro na tela'''
        self.tela.blit(self.imagem, self.rect)