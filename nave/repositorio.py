import pygame
import sys

#PYGAME:
pygame.init() #- sempre que utilizar a biblioteca pygame

tela = pygame.display.set_mode((600,400)) #- define tamanho da tela
    # tela.fill(255,255,255) #- preenche a tela com cores RGB
pygame.display.set_caption("Nave") #- define o nome da tela
pygame.display.flip() # dá um refresh na tela

evento = pygame.event.get() #- captura eventos de entrada de mouse/teclado
    # evento.type   #- propriedade do objeto evento que retorna seu tipo
    # pygame.QUIT    #- evento de clicar no 'X' para sair da tela


#SYS:
sys.exit() #- fecha a janela, tela

#OUTROS:
# __name__ == '__main__'  #- garante que códigos que estiverem em outros módulos
                          #- não sejam executados. É como se tudo o que eu colocar
                          #- aqui, fosse tratato como variável local. Não permite
                          #- a execução dos códigos, aqui inseridos, por outros
                          #- módulos

# obj1 = Nave()          #- cria um objeto do tipo de clase Nave
# obj1.roda_jogo()       #- intância do obj1 chama o método roda_jogo, o qual
                         #- pertence à classe Nave