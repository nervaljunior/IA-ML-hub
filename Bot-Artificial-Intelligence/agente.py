import random
import time
from os import system
from lixeira import *
from main import *
caminho_percorrido=[] 
posicao_atual=None
posicao_lixo=(19,19)



def aleatorio(x, y):
    # Verifica as direções possíveis, levando em consideração a posição do robô na matriz
    possiveis_direcoes = []
    #percept()
    if x > 0:  # cima
        possiveis_direcoes.append((-1, 0))
    if x < 19:  #  baixo
        possiveis_direcoes.append((1, 0))
    if y > 0:  #  esquerda
        possiveis_direcoes.append((0, -1))
    if y < 19:  #  direita
        possiveis_direcoes.append((0, 1))

    # Se não há direções possíveis, retorna (0,0)
    if len(possiveis_direcoes) == 0:
        return (0, 0)
    
    # Escolhe uma direção aleatória dentre as possíveis
    direcao = random.choice(possiveis_direcoes)
    return direcao


def levar_lixo(tipo_lixo, posicao_atual, matriz):
    # Observe a posição atual e vá até a posição (19, 19) da matriz
    pos_x_atual, pos_y_atual = posicao_atual
    pos_x_lixo, pos_y_lixo = 19, 19
    tamanho_matriz = len(matriz)

    while pos_x_atual != pos_x_lixo or pos_y_atual != pos_y_lixo:
        # Move o robô na direção x se ainda não estiver na posição correta
        if pos_x_atual != pos_x_lixo:
            if pos_x_atual < pos_x_lixo:
                pos_x_proximo = min(pos_x_atual + 1, tamanho_matriz - 1)
                if matriz[pos_x_proximo][pos_y_atual] != "R" and matriz[pos_x_proximo][pos_y_atual] != "O":
                    pos_x_atual = pos_x_proximo
            else:
                pos_x_proximo = max(pos_x_atual - 1, 0)
                if matriz[pos_x_proximo][pos_y_atual] != "R" and matriz[pos_x_proximo][pos_y_atual] != "O":
                    pos_x_atual = pos_x_proximo

        # Move o robô na direção y se ainda não estiver na posição correta
        if pos_y_atual != pos_y_lixo:
            if pos_y_atual < pos_y_lixo:
                pos_y_proximo = min(pos_y_atual + 1, tamanho_matriz - 1)
                if matriz[pos_x_atual][pos_y_proximo] != "R" and matriz[pos_x_atual][pos_y_proximo] != "O":
                    pos_y_atual = pos_y_proximo
            else:
                pos_y_proximo = max(pos_y_atual - 1, 0)
                if matriz[pos_x_atual][pos_y_proximo] != "R" and matriz[pos_x_atual][pos_y_proximo] != "O":
                    pos_y_atual = pos_y_proximo

        # Atualiza a matriz com a nova posição do robô
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"  # Limpa a posição anterior do robô
        matriz[pos_x_atual][pos_y_atual] = "A"  # Marca a nova posição do robô

        # Imprime a matriz atualizada na tela
        for i in range(tamanho_matriz):
            for j in range(tamanho_matriz):
                print(matriz[i][j], end=" ")
            print()
        print("")
        print(f'Levando lixo {tipo_lixo.upper()} para lixeira')

        print()
        point = pontuacao()
        print(f'Pontuação: {point}')

        time.sleep(0.1)
        system("cls")

        # Atualiza a posição atual do robô
        posicao_atual = (pos_x_atual, pos_y_atual)

    # Após chegar à posição (19, 19) da matriz, chama a função receber_lixo
    receber_lixo(tipo_lixo)

    matriz[pos_x_atual][pos_y_atual] = "X"

    return matriz

'''direcoes = ["cima", "baixo", "esquerda", "direita"]
        obstaculos = []
        for direcao in direcoes:
            if direcao == "cima":
                pos_x_proximo = max(pos_x_atual - 1, 0)
                if matriz[pos_x_proximo][pos_y_atual] != "R" and matriz[pos_x_proximo][pos_y_atual] != "O":
                    obstaculos.append(matriz[pos_x_proximo][pos_y_atual])
                else:
                    obstaculos.append("O")
            elif direcao == "baixo":
                pos_x_proximo = min(pos_x_atual + 1, tamanho_matriz - 1)
                if matriz[pos_x_proximo][pos_y_atual] != "R" and matriz[pos_x_proximo][pos_y_atual] != "O":
                    obstaculos.append(matriz[pos_x_proximo][pos_y_atual])
                else:
                    obstaculos.append("O")
            elif direcao == "esquerda":
                pos_y_proximo = max(pos_y_atual - 1, 0)
                if matriz[pos_x_atual][pos_y_proximo] != "R" and matriz[pos_x_atual][pos_y_proximo] != "O":
                    obstaculos.append(matriz[pos_x_atual][pos_y_proximo])
                else:
                    obstaculos.append("O")
            elif direcao == "direita":
                pos_y_proximo = min(pos_y_atual + 1, tamanho_matriz - 1)
                if matriz[pos_x_atual][pos_y_proximo] != "R" and matriz[pos_x_atual][pos_y_proximo] != "O":
                    obstaculos.append(matriz[pos_x_atual][pos_y_proximo])
                else:
                    obstaculos.append("O")

        # Escolhe a direção com menor obstáculos e atualiza a posição atual
        proxima_direcao = direcoes[obstaculos.index(min(obstaculos))]
        if proxima_direcao == "cima":
            pos_x_atual = max(pos_x_atual - 1, 0)
        elif proxima_direcao == "baixo":
            pos_x_atual = min(pos_x_atual + 1, tamanho_matriz - 1)
        elif proxima_direcao == "esquerda":
            pos_y_atual = max(pos_y_atual - 1, 0)
        elif proxima_direcao == "direita":
            pos_y_atual = min(pos_y_atual + 1, tamanho_matriz - 1)

    return pos_x_atual, pos_y_atual

'''
def react_based_models(matriz):
    global caminho_percorrido, posicao_atual
    
    # Encontra a posição atual do robô
    posicao_lixo = (19, 19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] == "A":
                posicao_atual = (i, j)
                break
    
    i, j = posicao_atual
    
    # Movimentação aleatória, evitando áreas já percorridas
    while True:
        i_novo, j_novo = 0, 0
        direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # direções possíveis: direita, baixo, esquerda, cima
        for direcao in direcoes:
            nova_i = i + direcao[0]
            nova_j = j + direcao[1]
            if nova_i >= 0 and nova_i < 20 and nova_j >= 0 and nova_j < 20 and (nova_i, nova_j) not in caminho_percorrido:
                i_novo, j_novo = direcao
                break
        
        if i_novo == 0 and j_novo == 0:
            # Se não encontrar uma nova direção, retorna a matriz atual
            return matriz
        
        # Move o robô para a nova posição
        nova_i = i + i_novo
        nova_j = j + j_novo
        
        if matriz[nova_i][nova_j] in ['R', 'O']:
            lixo = 'reciclável' if matriz[nova_i][nova_j] == 'R' else 'orgânico'
            print(f'levando lixo {lixo} para lixeira')
            matriz[nova_i][nova_j] = "_"
            levar_lixo(lixo, posicao_atual, matriz)
            matriz[posicao_atual[0]][posicao_atual[1]] = "_"
            matriz[19][18] = "A"
        else:
            matriz[posicao_atual[0]][posicao_atual[1]] = "_"
            matriz[nova_i][nova_j] = "A"
            posicao_atual = (nova_i, nova_j)
            caminho_percorrido.append(posicao_atual)
            return matriz


def ainda_nao_passei(x, y, matriz):
    global caminho_percorrido, posicao_atual

    # Verifica se a célula atual não está na lista de células percorridas
    if (x, y) not in caminho_percorrido:
        # Verifica se há lixo na célula
        if matriz[x][y] in ['R', 'O']:
            lixo = 'reciclável' if matriz[x][y] == 'R' else 'orgânico'

            # Calcula o deslocamento necessário para chegar à célula com lixo
            deslocamento_i = x - posicao_atual[0]
            deslocamento_j = y - posicao_atual[1]

            # Movimento do robô de acordo com o deslocamento necessário
            if deslocamento_i < 0:
                # Movimento para cima
                matriz[posicao_atual[0] - 1][posicao_atual[1]] = "A"
                matriz[posicao_atual[0]][posicao_atual[1]] = "_"
                posicao_atual = (posicao_atual[0] - 1, posicao_atual[1])
            elif deslocamento_i > 0:
                # Movimento para baixo
                matriz[posicao_atual[0] + 1][posicao_atual[1]] = "A"
                matriz[posicao_atual[0]][posicao_atual[1]] = "_"
                posicao_atual = (posicao_atual[0] + 1, posicao_atual[1])
            elif deslocamento_j < 0:
                # Movimento para esquerda
                matriz[posicao_atual[0]][posicao_atual[1] - 1] = "A"
                matriz[posicao_atual[0]][posicao_atual[1]] = "_"
                posicao_atual = (posicao_atual[0], posicao_atual[1] - 1)
            elif deslocamento_j > 0:
                # Movimento para direita
                matriz[posicao_atual[0]][posicao_atual[1] + 1] = "A"
                matriz[posicao_atual[0]][posicao_atual[1]] = "_"
                posicao_atual = (posicao_atual[0], posicao_atual[1] + 1)

            caminho_percorrido.append(posicao_atual)

    return matriz


#nessa função ele verifica as possições que ele ja passou, se ja onde ele passou nao tiver lixo , ele te que evitar ir novamente lá


def based_utility(matriz):
    #começa como simples e se tiver um lixo reciclavel ele armazena na memoria e depois vai buscar 
    #baseado em utilidades tem felicidade, ou seja, ele liga para pontuação 
    # Encontra a posição atual do robô
    posicao_lixo=(19,19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                posicao_atual = (i, j)
                break
                
    i,j=posicao_atual
    adjacent=percept_r(i,j,matriz)        
    if adjacent:
        melhor_lixo = None
        i_novo, j_novo=adjacent
        melhor_lixo = (i_novo, j_novo)
        i_novo, j_novo = melhor_lixo
        # Move o robô para a posição do lixo com a maior pontuação
        if(posicao_atual==posicao_lixo):
            matriz[posicao_atual[0]][posicao_atual[1]] = "X"
            matriz[i][j] = "A"
            return matriz
        if(matriz[i][j]=="R" or matriz[i][j]=="O"): 
            if matriz[i][j]=='R':
                lixo='reciclável'
                print(f'levando lixo {lixo} para lixeira')
                matriz[i][j] = "_"
                levar_lixo(lixo,posicao_atual,matriz)
            elif matriz[i][j]=='O':
                lixo='orgânico'
                print(f'levando lixo {lixo} para lixeira')
                matriz[i][j] = "_"
                levar_lixo(lixo,posicao_atual,matriz)
            matriz[posicao_atual[0]][posicao_atual[1]] = "_"
            matriz[19][18] = "A"
              
    i_novo,j_novo=aleatorio(i,j)
    i+=i_novo
    j+=j_novo
    
    # Move o robô para a nova posição
    if(posicao_atual==posicao_lixo):
        matriz[posicao_atual[0]][posicao_atual[1]] = "X"
        matriz[i][j] = "A"
        return matriz
    if(matriz[i][j]=="R" or matriz[i][j]=="O"): 
        if matriz[i][j]=='R':
            lixo='reciclável'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        elif matriz[i][j]=='O':
            lixo='orgânico'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[19][18] = "A"
    else:
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[i][j] = "A"
        return matriz
    
    #a percepção do de utilidade é que ele tem que dar preferencia para os lixos com maior pontuação 

def percept_r(i, j, matriz):
    #aqui eu tenho que dar uma percepção para ele dar preferencia aos lixos reciclaveis
    # Verifica se o lixo na posição atual é reciclável
    # Lista com as posições adjacentes ao robô
    adjacents = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

    # Verifica se há lixo reciclável nas posições adjacentes
    for x, y in adjacents:
        if x >= 0 and x < 20 and y >= 0 and y < 20:  # Verifica se a posição está dentro dos limites da matriz
            if matriz[x][y] == "R":
                return (x, y)  # Retorna a posição do lixo reciclável se encontrado

    # Se não houver lixo reciclável nas posições adjacentes, procura por lixo orgânico
    for x, y in adjacents:
        if x >= 0 and x < 20 and y >= 0 and y < 20:  # Verifica se a posição está dentro dos limites da matriz
            if matriz[x][y] == "O":
                return (x, y)  # Retorna a posição do lixo orgânico se encontrado

    # Se não houver lixo reciclável nem orgânico nas posições adjacentes, retorna None
    return None

def based_goals(matriz):
    # Encontra a posição atual do robô por objetivos
    # o objetivo dele é pegar todos os lixos
    posicao_lixo = (19, 19)
    posicao_atual = None
    for i in range(20):
        for j in range(20):
            if matriz[i][j] == "A":
                posicao_atual = (i, j)
                break

    i, j = posicao_atual

    i_novo, j_novo = andar_vertical(i, j)
    i += i_novo

    # Incrementa +1 em y (linha) a cada pulada de coluna (x)
    if j + j_novo >= 20:
        i += 1
        j = 0
    else:
        j += j_novo

    # Verifica se as posições estão dentro dos limites válidos da matriz
    if i < 0 or i >= 20 or j < 0 or j >= 20:
        print("Posição inválida!")
        # Leva o robô de volta para a linha 1, coluna 2
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        j += 1
        posicao_atual = i, j
        matriz[0][j] = "A"
        return matriz

    # Move o robô para a nova posição
    if posicao_atual == posicao_lixo:
        matriz[posicao_atual[0]][posicao_atual[1]] = "X"
        matriz[i][j] = "A"
        return matriz
    if matriz[i][j] == "R" or matriz[i][j] == "O":
        if matriz[i][j] == 'R':
            lixo = 'reciclável'
        elif matriz[i][j] == 'O':
            lixo = 'orgânico'
        print(f'levando lixo {lixo} para lixeira')
        matriz[i][j] = "_"
        levar_lixo(lixo, posicao_atual, matriz)
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[19][18] = "A"
    else:
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[i][j] = "A"
        return matriz


def andar_vertical(x, y):
    # o robô por objetivo anda na vertical até pegar um lixo, assim que pegar o lixo ele chama a função para levar a lixeira
    # depois de andar na vertical ele volta para posição inicial
    # se já tiver percorrido toda linha coluna 1 ele pula para coluna dois e assim sucessivamente
    # O robô anda na vertical até pegar um lixo e então retorna para a posição inicial da linha seguinte
    if x == 19:  # Se estiver na última linha
        return 1, +y  # Volta para a posição inicial da próxima coluna
    else:
        return 1, 0  # Move-se para baixo na mesma coluna

def percept(x, y, matriz):
    # Verifica as 8 células ao redor do robô
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # Verifica se a célula está dentro dos limites da matriz
            if 0 <= i < 20 and 0 <= j < 20:
                # Verifica se há lixo 
                if matriz[i][j] =='R':
                    lixo = 'reciclável'
                    
                    # Calcula o deslocamento da matriz necessário para chegar à célula com lixo
                    deslocamento_i = i - x
                    deslocamento_j = j - y

                # Função para fazer o movimento do robô de acordo com o deslocamento necessário
                    if deslocamento_i < 0:
                        #  cima
                        matriz[x-1][y] = "A"
                        matriz[x][y] = "_"
                        x -= 1
                    elif deslocamento_i > 0:
                        #  baixo
                        matriz[x+1][y] = "A"
                        matriz[x][y] = "_"
                        x += 1
                    elif deslocamento_j < 0:
                        #  esquerda
                        matriz[x][y-1] = "A"
                        matriz[x][y] = "_"
                        y -= 1
                    elif deslocamento_j > 0:
                        #  direita
                        matriz[x][y+1] = "A"
                        matriz[x][y] = "_"
                        y += 1
                        
                  # Coloca o robô na posição do lixo
                    levar_lixo(lixo, (i, j), matriz)
                    return (19,18)
                
                elif matriz[i][j] =='O':
                    lixo = 'orgânico'

                    # Calcula o deslocamento da matriz necessário para chegar à célula com lixo
                    deslocamento_i = i - x
                    deslocamento_j = j - y

                # Função para fazer o movimento do robô de acordo com o deslocamento necessário
                    if deslocamento_i < 0:
                        #  cima
                        matriz[x-1][y] = "A"
                        matriz[x][y] = "_"
                        x -= 1
                    elif deslocamento_i > 0:
                        #  baixo
                        matriz[x+1][y] = "A"
                        matriz[x][y] = "_"
                        x += 1
                    elif deslocamento_j < 0:
                        #  esquerda
                        matriz[x][y-1] = "A"
                        matriz[x][y] = "_"
                        y -= 1
                    elif deslocamento_j > 0:
                        # direita
                        matriz[x][y+1] = "A"
                        matriz[x][y] = "_"
                        y += 1
                        
                    # Coloca o robô na posição do lixo

                    # Chama a função para fazer o movimento do robô
                    levar_lixo(lixo, (i, j), matriz)
                    return (19,18)

                else:
                    return None

def react_simples(matriz):
    #aqui falta fazer a percepção do entorno que ta com bug
    #a primeira coisa que ele tem que fazer é verificaar se tem alguem no entorno
    # Encontra a posição atual do robô
    for i in range(20):
        for j in range(20):
            if matriz[i][j] =="A":
                #pegar o lixo que ta ao redor 
                '''posicao_atual=percept(i,j,matriz)
                if posicao_atual==None:'''
                posicao_atual = (i, j)
                break
                
    i,j=posicao_atual  
    #começa andar aleatoriaente
    i_novo,j_novo=aleatorio(i,j)
    i+=i_novo
    j+=j_novo
    
    # Move o robô para a nova posição
    if(posicao_atual==posicao_lixo):
        matriz[posicao_atual[0]][posicao_atual[1]] = "X"
        matriz[i][j] = "A"
        return matriz
    if(matriz[i][j]=="R" or matriz[i][j]=="O"):
        if matriz[i][j]=='R':
            lixo='reciclável'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        elif matriz[i][j]=='O':
            lixo='orgânico'
            print(f'levando lixo {lixo} para lixeira')
            matriz[i][j] = "_"
            levar_lixo(lixo,posicao_atual,matriz)
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[19][18] = "A"
    else:
        matriz[posicao_atual[0]][posicao_atual[1]] = "_"
        matriz[i][j] = "A"
        return matriz