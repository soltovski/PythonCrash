import sys
import pygame

class Nave:
    '''classe geral que gerencia comportamento do jogo'''

    def __init__(self):
        '''inicializa o jogo, e cria recursos do jogo'''
        pygame.init() #inerente ao pygame

        self.tela = pygame.display.set_mode((600,400)) #representa a tela do jogo
        pygame.display.set_caption("Nave")

    def roda_jogo(self):
        '''loop principal'''
        while True:
            #aguarda comando do teclado/mouse
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:#quando clicar no X, para sair da tela
                    sys.exit()

            #refresh na tela
            pygame.display.flip()

if __name__ == '__main__':
    #Cria uma instância do jogo e o executa
    ai = Nave() #cria objeto do tipo Nave
    ai.roda_jogo() #executa o método roda_jogo()
