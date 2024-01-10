import random

DIMENSOES_AMBIENTE = (20, 20)
NUMERO_LIXOS_ORGANICOS = 10
NUMERO_LIXOS_RECICLAVEIS = 5
VALOR_LIXO_ORGANICO = 1
VALOR_LIXO_RECICLAVEL = 5
POSICAO_INICIAL_ROBO = (1, 1)
POSICAO_LIXEIRA = (20, 20)

class Ambiente:
    def __init__(self):
        self.dimensoes = DIMENSOES_AMBIENTE
        self.lixos_organicos = set()
        self.lixos_reciclaveis = set()
        self.inicializar_ambiente()

    def inicializar_ambiente(self):
        for i in range(NUMERO_LIXOS_ORGANICOS):
            posicao = self.gerar_posicao_aleatoria()
            self.lixos_organicos.add(posicao)
        for i in range(NUMERO_LIXOS_RECICLAVEIS):
            posicao = self.gerar_posicao_aleatoria()
            self.lixos_reciclaveis.add(posicao)

    def gerar_posicao_aleatoria(self):
        x = random.randint(1, self.dimensoes[0])
        y = random.randint(1, self.dimensoes[1])
        return (x, y)

    def verificar_posicao_valida(self, posicao):
        return 1 <= posicao[0] <= self.dimensoes[0] and 1 <= posicao[1] <= self.dimensoes[1]

    def verificar_robô_na_lixeira(self, posicao):
        return posicao == POSICAO_LIXEIRA


class Robo:
    def __init__(self):
        self.posicao = POSICAO_INICIAL_ROBO
        self.conteudo_local = None

    def andar_esquerda(self):
        nova_posicao = (self.posicao[0], self.posicao[1] - 1)
        if Ambiente.verificar_posicao_valida(nova_posicao):
            self.posicao = nova_posicao

    def andar_direita(self):
        nova_posicao = (self.posicao[0], self.posicao[1] + 1)
        if Ambiente.verificar_posicao_valida(nova_posicao):
            self.posicao = nova_posicao

    def andar_cima(self):
        nova_posicao = (self.posicao[0] - 1, self.posicao[1])
        if Ambiente.verificar_posicao_valida(nova_posicao):
            self.posicao = nova_posicao

