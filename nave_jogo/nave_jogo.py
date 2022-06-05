import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import  Bullet

class Nave_jogo:
    '''classe geral que gerencia comportamento do jogo'''

    def __init__(self):
        '''inicializa o jogo, e cria recursos do jogo'''
        pygame.init() #inerente ao pygame

        self.settings = Settings()  # cria objeto do tipo Settings

        #self.tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.tela_lar = self.tela.get_rect().width
        #self.settings.tela_alt = self.tela.get_rect().height

        self.tela = pygame.display.set_mode((self.settings.tela_lar,self.settings.tela_alt)) #representa a tela do jogo
        pygame.display.set_caption("Nave")

        self.ship = Ship(self) #cria um objeto da classe Ship, e passa self como parâmentro
                               # que se refere à instância atual de Nave_jogo
        self.bullets = pygame.sprite.Group() #


    def roda_jogo(self):
        '''loop principal'''
        while True:
            #aguarda comando do teclado/mouse
            self._checa_eventos()
            self.ship.update()
            self.bullets.update() #chama update para cada elemento do grupo
            self._update_tela()


    def _checa_eventos(self):
        '''responde a eventos do mouse/teclado'''
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # quando clicar no X, para sair da tela
                sys.exit()
            elif evento.type == pygame.KEYDOWN:#se pressinar alguma tecla
                self._check_keydown_eventos(evento)

            elif evento.type == pygame.KEYUP: #se liberou uma tecla
                self._check_keyup_eventos(evento)

    def _check_keydown_eventos(self, evento):
        '''responde a teclas pressionadas'''
        if evento.key == pygame.K_RIGHT:  # essa tecla é 'direita'
            self.ship.vai_para_dir = True  # move a nave para a direita
        elif evento.key == pygame.K_LEFT:  # essa tecla é esquerda
            self.ship.vai_para_esq = True
        elif evento.key == pygame.K_q: #essa tecla é 'q'
            sys.exit()
        elif evento.key == pygame.K_SPACE:
            self._atira_bullet()

    def _check_keyup_eventos(self, evento):
        '''responde a teclas liberadas'''
        if evento.key == pygame.K_RIGHT:  # se a tecla liberada foi a 'seta direita'
            self.ship.vai_para_dir = False
        elif evento.key == pygame.K_LEFT:
            self.ship.vai_para_esq = False

    def _atira_bullet(self):
        '''cria uma nova bala e a adiciona ao grupo de balas'''
        nova_bala = Bullet(self)
        self.bullets.add(nova_bala)

    def _update_tela(self):
        # redesenhar a tela durante cada passagem de loop
        self.tela.fill(self.settings.tela_cor)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.desenha_bullet()

        # refresh na tela
        pygame.display.flip()


if __name__ == '__main__':
    #Cria uma instância do jogo e o executa
    ai = Nave_jogo() #cria objeto do tipo Nave
    ai.roda_jogo() #executa o método roda_jogo()
