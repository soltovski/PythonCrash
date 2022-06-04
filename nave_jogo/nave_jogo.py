import sys
import pygame
from settings import Settings
from ship import Ship

class Nave_jogo:
    '''classe geral que gerencia comportamento do jogo'''

    def __init__(self):
        '''inicializa o jogo, e cria recursos do jogo'''
        pygame.init() #inerente ao pygame

        self.settings = Settings()  # cria objeto do tipo Settings

        self.tela = pygame.display.set_mode((self.settings.tela_lar,self.settings.tela_alt)) #representa a tela do jogo
        pygame.display.set_caption("Nave")

        self.ship = Ship(self) #cria um objeto da classe Ship, e passa self como parâmentro
                               # que se refere à instância atual de Nave_jogo


    def roda_jogo(self):
        '''loop principal'''
        while True:
            #aguarda comando do teclado/mouse
            self._checa_eventos()
            self._update_tela()


    def _checa_eventos(self):
        '''responde a eventos do mouse/teclado'''
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # quando clicar no X, para sair da tela
                sys.exit()

    def _update_tela(self):
        # redesenhar a tela durante cada passagem de loop
        self.tela.fill(self.settings.tela_cor)
        self.ship.blitme()

        # refresh na tela
        pygame.display.flip()


if __name__ == '__main__':
    #Cria uma instância do jogo e o executa
    ai = Nave_jogo() #cria objeto do tipo Nave
    ai.roda_jogo() #executa o método roda_jogo()
