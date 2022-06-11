class Config:
    '''Classe que gerencia as configurações do jogo'''

    def __init__(self):
        """inicializa as preferencias do jogo"""
        #configurações de tela
        self.tela_lar = 600
        self.tela_alt = 750
        self.cor_fundo = (255,255,255)

        #configurações do carro
        self.carro_veloc = 0.8 #ponto flutuante

        #preferências de veiculo
        self.veic_veloc = 0.2
        self.frota_descida_veloc = 10
        self.direcao_frota = 1 # 1 para direita, -1 para esquerda