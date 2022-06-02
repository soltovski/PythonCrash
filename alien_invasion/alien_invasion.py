
import sys #biblioteca para controles de I/O
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Classe geral para gerenciar o jogo'''

    def __init__(self):
        '''Inicializa e cria os recursos do jogo'''
        pygame.init() #inicializa o background

        self.settings = Settings()#cria um objeto do tipo settings
        self.screen = pygame.display.set_mode(
             (self.settings.screen_width,self.settings.screen_height))#cria e define o tamanho da tela
        pygame.display.set_caption("Alien Invasion") #define o nome

        self.ship = Ship(self)

    def run_game(self):
        '''Loop principal do jogo'''
        while True:
            #espera por comandos do mouse/teclado
            for event in pygame.event.get(): #dentro loop, sempre ativo
                if event.type == pygame.QUIT:
                    sys.exit()

            #redesenha a tela durante cada passagem o loop while
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #refresh na tela, cria a 'ilusão' de movimento
            pygame.display.flip()

if __name__ == '__main__': #não executa sozinho, apenas se chamado
    #cria uma instância e roda o jogo:
    ai = AlienInvasion()
    ai.run_game()

























'''import sys
import pygame
from settings import Settings
from ship import Ship

def roda_jogo():
    #inicializa o jogo, prefencias e cria o layout (tela de objetos)
    pygame.init()
    ia_pref = Settings()
    screen = pygame.display.set_mode((ia_pref.screen_largura,ia_pref.screen_altura))
    pygame.display.set_caption("Alien Invasion")

    #Cria a nave
    ship = Ship(screen)

    #define a cor da tela de fundo
    cor_fundo=(ia_pref.cor_fundo)
    ship.blitme()

    #inicializa o loop principal do jogo
    while True:

     #aguarda entrada do teclado ou mouse
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
                sys.exit()
    #recolore o fundo a cada iteração
    screen.fill(cor_fundo)

    #exibe a última tela
    pygame.display.flip()

roda_jogo()
'''