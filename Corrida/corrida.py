'''Criação de um jogo de corrida parecido com: https://www.youtube.com/watch?v=5Q5-QNfmsbQ'''
import sys
import pygame
from config import Config
from carro import Carro

class Corrida:
    '''Classe que gerencia o jogo'''

    def __init__(self):
        '''inicializa o jogo e cria recursos do jogo'''
        pygame.init()
        self.config = Config() #cria objeto do tipo Config

        self.tela = pygame.display.set_mode((self.config.tela_lar,self.config.tela_alt))
        pygame.display.set_caption("Corrida")

        self.carro_driver = Carro(self)#cria obj do tipo Carro, já passando suas propriedades

    def roda_jogo(self):
        '''loop principal do jogo'''
        while True:
            #aguarda por eventos de teclado/mouse
            self._checa_eventos()
            self.carro_driver.att_pos_carro()
            self._att_tela()

    def _checa_eventos(self):
        #responde a eventos da teclado/mouse
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            elif evento.type == pygame.KEYDOWN:#apertou uma tecla
                self._checa_tecla_press(evento)
            elif evento.type == pygame.KEYUP:#liberou uma tecla
                self._checa_tecla_lib(evento)

    def _checa_tecla_press(self, evento):
        '''responde à tecla pressionada'''
        if evento.key == pygame.K_RIGHT:  # essa tecla é direita
            self.carro_driver.flag_mov_direita = True
        elif evento.key == pygame.K_LEFT:  # essa tecla é esquerda
            self.carro_driver.flag_mov_esquerda = True

    def _checa_tecla_lib(self, evento):
        '''responde à tecla liberada'''
        if evento.key == pygame.K_RIGHT:  # a tecla da direita
            self.carro_driver.flag_mov_direita = False
        elif evento.key == pygame.K_LEFT:  # a tecla da esquerda
            self.carro_driver.flag_mov_esquerda = False


    def _att_tela(self):
        # att cor de fundo durante a passagem de loop
        self.tela.fill(self.config.cor_fundo)
        self.carro_driver.blitme()

        # dá um refresh na tela, cria ilusão de movimento
        pygame.display.flip()

if __name__ == '__main__': #faz com que os pacotes importados não executem automaticamente seus main
    #cria uma instância do jogo e a roda o jogo
    obj_corrida = Corrida()
    obj_corrida.roda_jogo()




