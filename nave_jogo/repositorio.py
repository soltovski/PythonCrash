import pygame   #- importa um módulo completo, com todas suas classes
import sys
from settings import Settings #- import apenas uma classe de um módulo

#PYGAME:
pygame.init() #- sempre que utilizar a biblioteca pygame

tela = pygame.display.set_mode((600,400)) #- define tamanho da tela
    # tela.fill(255,255,255)         #- preenche a tela com cores RGB
    # tela_tect = tela.get_rect()    #- retorna o rect -origem (0,0)TOPLEFT- da tela
                                     #- ou outro surface (tela e objetos dentro dela)
    # tela_rect.midbottom #- retorna a posição rect inferior central de um surface

    #centralizar: centerx, centery, center
    #borda: top, bottom, left, right
    #outros: midbottom, midtop, midleft, midright

pygame.display.set_caption("Nave") #- define o nome da tela
pygame.display.flip() # dá um refresh na tela

pygame.image.load('imagens/ship.bmp')  #- carrega um arquivo de imagem (surface)
    #.imagem_nave.get_rect()           #- retorna o rect de um.bmp

evento = pygame.event.get() #- captura eventos de entrada de mouse/teclado
    # evento.type   #- propriedade do objeto evento que retorna seu tipo
    # pygame.QUIT    #- evento de clicar no 'X' para sair da tela
    # pygame.KEYDOWN  #- alguma tecla é pressionada
    # evento.key    #- retorna uma tecla que foi pressionada
    # pygame.K_RIGHT   #- tecla "seta da direita" é pressionada


#SYS:
sys.exit() #- fecha a janela, tela

#OUTROS:
# __name__ == '__main__'  #- garante que códigos que estiverem em outros módulos
                          #- não sejam executados. É como se tudo o que eu colocar
                          #- aqui, fosse tratato como variável local. Não permite
                          #- a execução dos códigos, aqui inseridos, por outros
                          #- módulos

# obj1 = Nave_jogo()          #- cria um objeto do tipo de clase Nave
# obj1.roda_jogo()       #- intância do obj1 chama o método roda_jogo, o qual
                         #- pertence à classe Nave