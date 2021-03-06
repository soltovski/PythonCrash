'''Criação de um jogo de corrida parecido com: https://www.youtube.com/watch?v=5Q5-QNfmsbQ'''
import sys
import pygame
import random
from config import Config
from carro import Carro
from veiculo import Veiculo


class Corrida:
    '''Classe que gerencia o jogo'''

    def __init__(self):
        '''inicializa o jogo e cria recursos do jogo'''
        pygame.init()
        self.config = Config() #cria objeto do tipo Config


        self.tela = pygame.display.set_mode((self.config.tela_lar,self.config.tela_alt))
        pygame.display.set_caption("Corrida")

        self.carro_driver = Carro(self)#cria obj do tipo Carro, já passando suas propriedades

        self.veiculos = pygame.sprite.Group()
        self._cria_frota()



    def roda_jogo(self):
        '''loop principal do jogo'''
        while True:
            #aguarda por eventos de teclado/mouse
            self._checa_eventos()
            self.carro_driver.att_pos_carro()
            self._update_veiculos()
            self._att_tela()

    def _cria_frota(self):
        '''cria uma frota de veículos'''
        #cria um veículo e acha o numero de veiculos por linha
        #espaçpo entre veiculos é igual è própria largura de um veiculo
        veiculo = Veiculo(self)
        veic_larg, veic_alt = veiculo.rect.size
        espaco_x_disp = self.config.tela_lar - (2 * veic_larg)
        num_veic_x = espaco_x_disp // (2 * veic_larg)

        #determina o numero de linhas de veiculos que aparecerão na tela
        carro_alt = self.carro_driver.rect.height
        espaco_y_disp = (self.config.tela_alt -
                         (3 * veic_alt) - carro_alt)
        num_linhas = espaco_y_disp // (2 * veic_alt)

        #cria tela cheia de veiculos
        for num_linha in range(num_linhas):
            for veic_num in range(num_veic_x):
              self._cria_veic(veic_num, num_linha)


    def _cria_veic(self, veic_num, num_linha):
        '''cria um veiculo e o põe na linha'''
        veiculo = Veiculo(self)
        veic_larg, veic_alt = veiculo.rect.size
        veiculo.x = veic_larg + 2 * veic_larg * veic_num
        veiculo.rect.x = veiculo.x
        veiculo.rect.y = veiculo.rect.height + 2 * veiculo.rect.height * num_linha
        if random.randint(0, 2) == 0:  # cria quantidade aleatória de veiculos
            self.veiculos.add(veiculo)  # quanto maior 'y', menos veiculos



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
        elif evento.key == pygame.K_q:
            sys.exit()

    def _checa_tecla_lib(self, evento):
        '''responde à tecla liberada'''
        if evento.key == pygame.K_RIGHT:  # a tecla da direita
            self.carro_driver.flag_mov_direita = False
        elif evento.key == pygame.K_LEFT:  # a tecla da esquerda
            self.carro_driver.flag_mov_esquerda = False

    def _checa_frota_borda(self):
        '''responde se algum veiculo tocar a borda'''
        for veiculo in self.veiculos.sprites():
            if veiculo.checa_bordas():
                self._muda_direcao_frota()
                break

    def _muda_direcao_frota(self):
        '''abaixa toda a frota e muda a sua direcao'''
        for veiculo in self.veiculos.sprites():
            veiculo.rect.y += self.config.frota_descida_veloc
        self.config.direcao_frota *= -1


    def _update_veiculos(self):
        '''Atualiza a posição de todos os veiculos na frota e checa se frota tocou borda'''
        self._checa_frota_borda()
        self.veiculos.update()

    def _att_tela(self):
        # att cor de fundo durante a passagem de loop
        self.tela.fill(self.config.cor_fundo)
        self.carro_driver.blitme()

        self.veiculos.draw(self.tela)

        # dá um refresh na tela, cria ilusão de movimento
        pygame.display.flip()

if __name__ == '__main__': #faz com que os pacotes importados não executem automaticamente seus main
    #cria uma instância do jogo e a roda o jogo
    obj_corrida = Corrida()
    obj_corrida.roda_jogo()




