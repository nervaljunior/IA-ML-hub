import time
from array import *
from os import system
from matriz import *
from agente import *
from lixeira import *

if __name__ == "__main__":
    ambiente = gerar_ambiente()
    fim = True
    
    tempo_inicial = time.time()  # Registro do tempo inicial
    while fim:
        imprime(ambiente)
        time.sleep(0)
        system("cls")
        react_simples(ambiente)
        fim = verifica_matriz(ambiente)
    tempo_final = time.time()  # Registro do tempo final
    tempo_total = tempo_final - tempo_inicial  # Cálculo do tempo total de execução

    # Cálculo das horas, minutos e segundos
    horas, resto = divmod(tempo_total, 3600)
    minutos, segundos = divmod(resto, 60)

    point = pontuacao()
    print(f'Pontuação: {point}')
    print(f'Programa finalizado.')
    print(f'Tempo total de execução: {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos.')

