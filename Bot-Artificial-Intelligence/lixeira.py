pont = 0

def receber_lixo(tipo_lixo):
    global pont
    capacidade = {'orgânico': 0, 'reciclável': 0}
    capacidade[tipo_lixo] += 1
    quant = tuple(capacidade.values())
    x, y = quant
    y *= 5
    pont += y + x

def pontuacao():
    global pont
    return pont



        