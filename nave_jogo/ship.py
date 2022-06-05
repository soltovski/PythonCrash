import pygame

class Ship:
    '''Classe que gerencia a nave'''

    def __init__(self, parametro): #referência para a instância atual.
                                    #dá à Ship, acesso a todos os recursos
                                    # defidos em Nave_jogo
        '''inicializa a nave e seta sua posicao de origem'''
        self.tela = parametro.tela # tela_ship recebe 'tela' de nave_jogo
        self.tela_rect = parametro.tela.get_rect() # atribui o rect da tela
                                    # de nave_jogo à tela_ship_rect
        self.settings = parametro.settings #

        #carrega a imagem da nave e pega seu rect
        self.imagem_nave = pygame.image.load('imagens/ship.bmp')#carrega imagem
        self.ship_rect = self.imagem_nave.get_rect() #

        #começa cada nova nave no fundo central da tela
        self.ship_rect.midbottom = self.tela_rect.midbottom #o rect inferior central
                                    # da figura da nave será o mesmo do rect inferior
                                    # central da tela_ship
        #grava um valor decimal para a posição horizontal da nave
        self.pos_x=float(self.ship_rect.x)

        #flag tecla continuamente pressionada
        self.vai_para_dir = False
        self.vai_para_esq = False

    def update(self):
        '''atualiza a posição da nave basedo na flag'''
        #atualiza o valor da posição decimal x, não do rect
        if self.vai_para_dir:
            self.pos_x += self.settings.veloc_ship #movimenta a figura da nave para a direita
        if self.vai_para_esq:
            self.pos_x -= self.settings.veloc_ship   #movimenta a figura da nave para a esquerda

        #Atualiza o rect a partir de pos_x
        self.ship_rect.x = self.pos_x

    def blitme(self):
        '''faz aparecer a imagem da nave na posicao indicada'''
        self.tela.blit(self.imagem_nave, self.ship_rect)

