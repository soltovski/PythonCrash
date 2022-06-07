
import sys #biblioteca para controles de I/O
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''Classe geral para gerenciar o jogo'''

    def __init__(self):
        '''Inicializa e cria os recursos do jogo'''
        pygame.init() #inicializa o background

        self.settings = Settings()#cria um objeto do tipo settings


        self.screen = pygame.display.set_mode(
             (0,0),pygame.FULLSCREEN)#cria e define o tamanho da tela
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion") #define o nome

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        '''Loop principal do jogo'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _create_fleet(self):
        '''Cria um esquadrão de aliens'''
        #cria um alien
        alien = Alien(self)
        self.aliens.add(alien) # um obj do tipo alien é add ao vetor sprite de aliens


    def _check_events(self):
        #responde a eventos do mouse/teclado
        for event in pygame.event.get():  # dentro loop, sempre ativo
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:#se uma tecla é pressionada
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: #tecla deixa de ser pressionada
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        '''responde à tecla pressionada'''
        if event.key == pygame.K_RIGHT:  # essa tecla é direita
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # essa tecla é esquerda
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #se pressionar ' Q'
            sys.exit() #sai do programa
        elif event.key == pygame.K_SPACE:#se pressionar barra de espaço
            self._fire_bullet() #dispara bala

    def _check_keyup_events(self,event):
        '''responde à tecla liberada'''
        if event.key == pygame.K_RIGHT:  # liberou a tecla que pressionava direita
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:  # liberou a tecla que pressionava esquerda
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''cria uma nova bala e a adiciona ao grupo de balas'''
        if len(self.bullets) < self.settings.bullets_allowed:#limita a qtd de balas em jogo
            new_bullet = Bullet(self) #cria uma instancia do tipo Bullet
            self.bullets.add(new_bullet)#addiciona ao grupo de bullets

    def _update_bullets(self):
        '''atualiza a posicao das balas e elimina as antigas'''
        #atualiza a posicão das balas
        self.bullets.update()

        # elimina as balas que sumirem da tela
        for bullet in self.bullets.copy():  # não tem como remover um elemento dentro de uma lista em execução num for
            # então faço o for varrer uma cópia dessa lista, assim ele pode remover os elementos do self.bullets
            if bullet.rect.bottom <= 0:  # se o fundo da figura tocar y0
                self.bullets.remove(bullet)
        # print(len(self.bullets)) exibe NO TERMINAL quantos bullets existem em execução

    def _update_screen(self):
        # atualiza as imagens da tela e tela de fundo
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() #chama a função draw_bullet de Bullet
        self.aliens.draw(self.screen)    #desenha na surface tela


        # refresh na tela, cria a 'ilusão' de movimento
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