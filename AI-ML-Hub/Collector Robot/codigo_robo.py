import random
import tkinter as tk

class Lixeira:
    def __init__(self, posicao):
        self.posicao = posicao
        self.capacidade = {'orgânico': 0, 'reciclável': 0}

    def receber_lixo(self, tipo_lixo, quantidade):
        self.capacidade[tipo_lixo] += quantidade

class Robo:
    def __init__(self, posicao, lixeira):
        self.posicao = posicao
        self.lixo = None
        self.pontuacao = 0
        self.lixeira = lixeira
        self.movimentos = {'esquerda': (0, -1), 'direita': (0, 1), 'cima': (-1, 0), 'baixo': (1, 0)}

    def coletar_lixo(self, tipo_lixo):
        if self.lixo is None:
            if self.ambiente[self.posicao[0]-1][self.posicao[1]-1][tipo_lixo] > 0:
                self.lixo = tipo_lixo
                return True
        return False

    def largar_lixo(self):
        if self.lixo is not None:
            tipo_lixo = self.lixo
            quantidade = self.ambiente[self.posicao[0]-1][self.posicao[1]-1][tipo_lixo]
            if quantidade > 0:
                self.lixo = None
                self.ambiente[self.posicao[0]-1][self.posicao[1]-1][tipo_lixo] -= 1
                self.lixeira.receber_lixo(tipo_lixo, 1)
                self.pontuacao += 1
                return True
        return False

    def andar(self, direcao):
        if direcao in self.movimentos:
            dx, dy = self.movimentos[direcao]
            nova_pos = (self.posicao[0] + dx, self.posicao[1] + dy)
            if 1 <= nova_pos[0] <= self.linhas and 1 <= nova_pos[1] <= self.colunas:
                self.posicao = nova_pos
                return True
        return False

    def voltar_lixeira(self):
        if self.lixo is not None:
            if self.posicao == self.lixeira.posicao:
                self.largar_lixo()
                return True
            else:
                caminho = self.caminho_livre(self.lixeira.posicao)
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
                    if nova_pos and self.ambiente[nova_pos[0]-1][nova_pos[1]-1]['vazio']:
                        nova_caminho = list(caminho)
                        nova_caminho.append(direcao)
                        fila.append(nova_caminho)
                visitados.add(posicao_atual)
        return None

    def proxima_posicao(self,destino, direcao):
        dx, dy = self.movimentos[direcao]
        nova_pos = (self.posicao[0] + dx, self.posicao[1] + dy)
        if 1 <= nova_pos[0] <= self.linhas and 1 <= nova_pos[1] <= self.colunas and nova_pos != destino:
            return nova_pos
        return None
    

class Ambiente :
    def iniciar_ambiente(self):
    # Cria a matriz do ambiente e define a posição da lixeira
        self.ambiente = []
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                # Inicializa o ambiente com todos os locais vazios
                linha.append({'orgânico': 0, 'reciclável': 0, 'vazio': True})
            self.ambiente.append(linha)
        self.ambiente[self.Lixeira.posicao[0]-1][self.Lixeira.posicao[1]-1]['vazio'] = False

    def posicionar_lixo(self, tipo_lixo, quantidade):
        # Posiciona um determinado tipo de lixo em uma posição aleatória do ambiente
        posicao = None
        while posicao is None:
            i = random.randint(0, self.linhas-1)
            j = random.randint(0, self.colunas-1)
            if self.ambiente[i][j]['vazio']:
                self.ambiente[i][j][tipo_lixo] += quantidade
                self.ambiente[i][j]['vazio'] = False
                posicao = (i+1, j+1)

    def posicionar_lixos(self, orgânico=0, reciclável=0):
        # Posiciona lixos orgânicos e recicláveis aleatoriamente no ambiente
        for i in range(orgânico):
            self.posicionar_lixo('orgânico', 1)
        for i in range(reciclável):
            self.posicionar_lixo('reciclável', 1)

    def imprimir_ambiente(self):
        # Imprime o estado atual do ambiente
        for i in range(self.linhas):
            for j in range(self.colunas):
                if not self.ambiente[i][j]['vazio']:
                    if self.ambiente[i][j]['orgânico'] > 0:
                        print(f"O({self.ambiente[i][j]['orgânico']})", end=' ')
                    if self.ambiente[i][j]['reciclável'] > 0:
                        print(f"R({self.ambiente[i][j]['reciclável']})", end=' ')
                else:
                    print(" . ", end=' ')
            print()

    def run(self, num_iteracoes):
        # Executa o ambiente por um determinado número de iterações
        for i in range(num_iteracoes):
            # Imprime o ambiente e a pontuação atual
            print(f"\nIteração {i+1}:")
            self.imprimir_ambiente()
            print(f"Pontuação: {self.robo.pontuacao}")
            
            # Verifica se o robô está com lixo e tenta levá-lo para a lixeira
            if self.robo.lixo is not None:
                self.robo.voltar_lixeira()
            
            # Coleta lixo da posição atual do robô
            self.robo.coletar_lixo('orgânico')
            self.robo.coletar_lixo('reciclável')
            
            # Decide a próxima ação do robô aleatoriamente
            acao = random.choice(['andar', 'largar_lixo'])
            if acao == 'andar':
                # Tenta andar para uma direção aleatória
                direcao = random.choice(list(self.robo.movimentos.keys()))
                self.robo.andar(direcao)

class Renderizador:
    def __init__(self, Ambiente, Robo):
        self.ambiente = Ambiente
        self.robo = Robo
        self.linhas = Ambiente.linhas
        self.colunas = Ambiente.colunas
        
        # Cria a janela e o canvas
        self.janela = tk.Tk()
        self.janela.title("Ambiente do Robô")
        self.canvas = tk.Canvas(self.janela, width=50*self.colunas, height=50*self.linhas)
        self.canvas.pack()
        
        # Desenha as células do ambiente
        for i in range(self.linhas):
            for j in range(self.colunas):
                cor = "white"
                if not self.ambiente.ambiente[i][j]['vazio']:
                    if self.ambiente.ambiente[i][j]['orgânico'] > 0:
                        cor = "brown"
                    if self.ambiente.ambiente[i][j]['reciclável'] > 0:
                        cor = "green"
                x0 = j*50
                y0 = i*50
                x1 = x0 + 50
                y1 = y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=cor, outline="black")
                
        # Desenha o robô
        x0 = (self.robo.posicao[1]-1)*50 + 5
        y0 = (self.robo.posicao[0]-1)*50 + 5
        x1 = x0 + 40
        y1 = y0 + 40
        self.canvas.create_oval(x0, y0, x1, y1, fill="red", outline="black")
        
        # Atualiza a janela
        self.janela.update()
    
    def atualizar(self):
        # Apaga o robô da sua posição anterior
        x0 = (self.robo.posicao_anterior[1]-1)*50 + 5
        y0 = (self.robo.posicao_anterior[0]-1)*50 + 5
        x1 = x0 + 40
        y1 = y0 + 40
        self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="white")
        
        # Desenha o robô na nova posição
        x0 = (self.robo.posicao[1]-1)*50 + 5
        y0 = (self.robo.posicao[0]-1)*50 + 5
        x1 = x0 + 40
        y1 = y0 + 40
        self.canvas.create_oval(x0, y0, x1, y1, fill="red", outline="black")
        
        # Atualiza a janela
        self.janela.update()
