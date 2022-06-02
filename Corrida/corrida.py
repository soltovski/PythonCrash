'''Criação de um jogo de corrida parecido com: https://www.youtube.com/watch?v=5Q5-QNfmsbQ'''
import sys
import pygame

class Corrida:
    '''Classe que gerencia o jogo'''

    def __init__(self):
        '''inicializa o jogo e cria recursos do jogo'''
        pygame.init()

        self.tela = pygame.display.set_mode((650,750))
        pygame.display.set_caption("Corrida")

    def roda_jogo(self):
        '''loop principal do jogo'''
        while True:
            #aguarda por eventos de teclado/mouse
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()

            #dá um refresh na tela, cria ilusão de movimento
            pygame.display.flip()

if __name__ == '__main__': #faz com que os pacotes importados não executem automaticamente seus main
    #cria uma instância do jogo e a roda o jogo
    obj_corrida = Corrida()
    obj_corrida.roda_jogo()




