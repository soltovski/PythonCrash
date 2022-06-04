import sys
import pygame
from settings import Settings

class Nave:
    '''classe geral que gerencia comportamento do jogo'''

    def __init__(self):
        '''inicializa o jogo, e cria recursos do jogo'''
        pygame.init() #inerente ao pygame

        self.settings = Settings()  # cria objeto do tipo Settings

        self.tela = pygame.display.set_mode((self.settings.tela_lar,self.settings.tela_alt)) #representa a tela do jogo
        pygame.display.set_caption("Nave")

        #define a cor de fundo da tela
       # self.cor_fundo = (230,230,230)




    def roda_jogo(self):
        '''loop principal'''
        while True:
            #aguarda comando do teclado/mouse
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:#quando clicar no X, para sair da tela
                    sys.exit()

            #redesenhar a tela durante cada passagem de loop
            self.tela.fill(self.settings.tela_cor)

            #refresh na tela
            pygame.display.flip()

if __name__ == '__main__':
    #Cria uma instância do jogo e o executa
    ai = Nave() #cria objeto do tipo Nave
    ai.roda_jogo() #executa o método roda_jogo()
