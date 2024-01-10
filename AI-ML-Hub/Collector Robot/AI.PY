# Criar uma matriz 2D 20x20 preenchida com valores de -1 para indicar que o local está vazio
matrix = [[-1 for _ in range(20)] for _ in range(20)]

import random

# Adicionar lixos orgânicos aleatoriamente
for i in range(10):
    row = random.randint(0, 19)
    col = random.randint(0, 19)
    while matrix[row][col] != -1:
        row = random.randint(0, 19)
        col = random.randint(0, 19)
    matrix[row][col] = 1

# Adicionar lixos recicláveis aleatoriamente
for i in range(5):
    row = random.randint(0, 19)
    col = random.randint(0, 19)
    while matrix[row][col] != -1:
        row = random.randint(0, 19)
        col = random.randint(0, 19)
    matrix[row][col] = 5
    
class Robo:
    def __init__(self):
        self.posicao = (1, 1)  # posição inicial do robô
        self.lixo = None  # lixo que o robô está carregando
        self.pontuacao = 0  # pontuação total do robô
        self.lixos_org = 10  # quantidade de lixos orgânicos no ambiente
        self.lixos_rec = 5  # quantidade de lixos recicláveis no ambiente
        self.lixeira = (20, 20)  # posição da lixeira
        self.movimentos = {'esquerda': (0, -1), 'direita': (0, 1), 'cima': (-1, 0), 'baixo': (1, 0)}  # movimentos possíveis do robô

    def coletar_lixo(self, tipo_lixo):
        if self.lixo is None:
            if tipo_lixo == 'orgânico':
                self.lixo = 1
            elif tipo_lixo == 'reciclável':
                self.lixo = 5
            return True
        return False

    def largar_lixo(self):
        if self.lixo is not None:
            self.pontuacao += self.lixo
            self.lixo = None
            return True
        return False

    def andar(self, direcao):
        if direcao in self.movimentos:
            dx, dy = self.movimentos[direcao]
            nova_pos = (self.posicao[0] + dx, self.posicao[1] + dy)
            if 1 <= nova_pos[0] <= 20 and 1 <= nova_pos[1] <= 20:  # Verifica se a nova posição está dentro dos limites do ambiente
                self.posicao = nova_pos
                return True
        return False


         
        

 

    def voltar_lixeira(self):
        if self.lixo is not None:
            if self.posicao == self.lixeira:
                self.largar_lixo()
                return True
            else:
                caminho = self.caminho_livre(self.lixeira)
                if caminho:
                    self.andar(caminho[0])
                    return True
        return False

    def caminho_livre(self, destino):
        fila = [[self.posicao]]
        visitados = set()
        while fila:
            caminho = fila.pop(0)
            posicao_atual = caminho[-1]
            if posicao_atual == destino:
                return caminho[1:]
            elif posicao_atual not in visitados:
                for direcao in self.movimentos:
                    nova_pos = self.proxima_posicao(posicao_atual, direcao)
                    if nova_pos and matrix[nova_pos[0]-1][nova_pos[1]-1] != -1:
                        nova_caminho = list(caminho)
                        nova_caminho.append(direcao)
                        fila.append(nova_caminho)
                visitados.add(posicao_atual)
        return None

    def proxima_posicao(self, posicao_atual, direcao):
        if direcao == 'esquerda':
            nova_pos = (posicao_atual[0], posicao_atual[1]-1)
        elif direcao == 'direita':
            nova_pos = (posicao_atual[0], posicao_atual[1]+1)
        elif direcao == 'cima':
            nova_pos = (posicao_atual[0]-1, posicao_atual[1])
        elif direcao == 'baixo':
            nova_pos = (posicao_atual[0]+1, posicao_atual[1])
        else:
            nova_pos = None

        if nova_pos and 1 <= nova_pos[0] <= 20 and 1 <= nova_pos[1] <= 20:
            return nova_pos
        else:
            return None

        

    
           