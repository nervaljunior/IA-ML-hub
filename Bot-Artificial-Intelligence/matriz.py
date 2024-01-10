import random
from main import *
from lixeira import *
point=0
def gerar_ambiente():
    # Cria uma matriz 20x20 preenchida com zeros
    matriz = [["_" for i in range(20)] for j in range(20)]

    # Define a posição inicial do robô e a lixeira
    lixeira="X"
    lixo_organico="O"
    lixo_reciclavel="R"
    
    matriz[0][0] = "A"
    matriz[19][19] = lixeira
    

    # Gera aleatoriamente 15 pares de coordenadas únicas
    coordenadas = set()
    while len(coordenadas) < 15:
        i = random.randint(0, 19)
        j = random.randint(0, 19)
        coordenadas.add((i, j))

    # Preenche as coordenadas com "O(organico)" ou "R(reciclavel)"
    contador_O = 0
    contador_R = 0
    for i, j in coordenadas:
        if contador_O < 10:
            matriz[i][j] = lixo_organico
            contador_O += 1
        else:
            matriz[i][j] = lixo_reciclavel
            contador_R += 1
    return matriz

def imprime(matriz):
    # Imprime a matriz na tela
    for i in range(20):
        for j in range(20):
            print(matriz[i][j], end=" ")
        print()
    print()
    print()
    point=pontuacao()
    print(f'pontuação: {point}') 
 
def verifica_matriz(matriz):
    for i in range(20):
        for j in range(20):
            if matriz[i][j] == "R" or matriz[i][j] == "O":
                return True
    return False   





        




        
