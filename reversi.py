# Reversi
import random
import sys


def drawBoard(board):
    # Essa funcao desenha o tabuleiro
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)

    for y in range(8):
        print(VLINE)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)


def resetBoard(board):
    # Essa funcao esvazia o tabuleiro
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
    # Pecas iniciais:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def getNewBoard():
    # Criar um tabuleiro novo
    board = []
    for i in range(8):
        board.append([' '] * 8)
    return board


def isValidMove(board, tile, xstart, ystart):
    # Retorna False se o movimento em xstart, ystart é invalido
    # Se o movimento é valido, retorna uma lista de casas que devem ser viradas após o movimento
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    board[xstart][ystart] = tile
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection  # first step in the direction
        y += ydirection  # first step in the direction
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    board[xstart][ystart] = ' '
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def isOnBoard(x, y):
    # Retorna True se a casa está no tabuleiro.
    return x >= 0 and x <= 7 and y >= 0 and y <= 7


def getBoardWithValidMoves(board, tile):
    # Retorna um tabuleiro com os movimentos validos
    dupeBoard = getBoardCopy(board)
    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard


def getValidMoves(board, tile):
    # Retorna uma lista de movimentos validos
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    # Determina o score baseado na contagem de 'X' e 'O'.
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}


def enterPlayerTile():
    # Permite que o player escolha ser X ou O
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Escolha suas peças: X ou O?')
        tile = input().upper()
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Escolhe aleatóriamente quem começa.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # Retorna True se o player quer jogar novamente
    print('Quer jogar novamente? (yes ou no)')
    return input().lower().startswith('y')


def makeMove(board, tile, xstart, ystart):
    # Coloca a peça no tabuleiro em xstart, ystart, e as peças do oponente
    # Retorna False se for um movimento invalido
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile

    return True


def getBoardCopy(board):
    # Faz uma cópia do tabuleiro e retorna a cópia
    dupeBoard = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard


def isOnCorner(x, y):
    # Retorna True se a posição x, y é um dos cantos do tabuleiro
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def getPlayerMove(board, playerTile):
    # Permite que o player insira sua jogada
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Insira seu movimento, ou insira quit para sair do jogo, ou hints para ativar/desativar dicas.')
        move = input().lower()
        if move == 'quit':
            return 'quit'

        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1

            if isValidMove(board, playerTile, x, y) == False:
                print("Essa não é uma jogada válida.")
                continue
            else:
                break

        else:
            print(
                'Essa não é uma jogada válida, digite o valor de x (1-8), depois o valor de y (1-8).')
            print('Por exemplo, 81 será o canto superior direito.')

    return [x, y]


def getComputerMove(board, computerTile):
    # Permite ao computador executar seu movimento
    possibleMoves = getValidMoves(board, computerTile)
    # randomiza a ordem dos possíveis movimentos
    random.shuffle(possibleMoves)
    # Escolhe a jogada que resulta em mais pontos
    return getBestMove(board, possibleMoves, computerTile)


def getBestMove(board, possibleMoves, computerTile):

    scoreDic = {}
    scoreHeuDic = {}
    bestHeuScore = -100
    bestScore = 100

    # Analisando a quantidade de novas peças
    # das possiveis jogadas
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        scoreDic[str(x) + ',' + str(y)] = score
        scoreHeuDic[str(x) + ',' + str(y)] = gameHeuristc(x, y)

    # Debuging
    # print("best score:", scoreDic)
    # print("best score heu:", scoreHeuDic)

    # Seleciona o maior valor de heuristica
    for key in scoreHeuDic.keys():
        if scoreHeuDic[key] > bestHeuScore:
            bestHeuScore = scoreHeuDic[key]
            x, y = getXeY(key)
            bestMove = [x, y]

    # Filtra movimentos possiveis
    # keys = []
    # for key in scoreHeuDic.keys():
    #     if scoreHeuDic[key] != bestHeuScore:
    #         keys.append(key)

    # for key in keys:
    #     scoreHeuDic.pop(key)
    #     scoreDic.pop(key)

    # Debuging
    # print("new best score:", scoreDic)
    # print("new best score heu:", scoreHeuDic)
    # print("move:", bestMove)
    # input('Pressione Enter para continuar.')
    return bestMove


def gameHeuristc(x, y):
    V = [
        [20, -3, 11, 8, 8, 11, -3, 20],
        [-3, -7, -4, 1, 1, -4, -7, -3],
        [11, -4, 2, 2, 2, 2, -4, 11],
        [8, 1, 2, -3, -3, 2, 1, 8],
        [8, 1, 2, -3, -3, 2, 1, 8],
        [11, -4, 2, 2, 2, 2, -4, 11],
        [-3, -7, -4, 1, 1, -4, -7, -3],
        [20, -3, 11, 8, 8, 11, -3, 20]
    ]

    return V[x][y]


def getXeY(string):
    x, y = string.split(',')
    return int(x), int(y)


def minimax(board, depth, maximizingPlayer, tile, alpha, beta):
    if depth == 0 or isTerminalNode(board):
        return evaluate(board, computerTile)

    if maximizingPlayer:
        maxEval = float('-inf')
        for x, y in getValidMoves(board, tile):
            dupeBoard = getBoardCopy(board)
            makeMove(dupeBoard, tile, x, y)
            eval = minimax(dupeBoard, depth - 1, False,
                           getOpponentTile(tile), alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for x, y in getValidMoves(board, tile):
            dupeBoard = getBoardCopy(board)
            makeMove(dupeBoard, tile, x, y)
            eval = minimax(dupeBoard, depth - 1, True,
                           getOpponentTile(tile), alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval


def isTerminalNode(board):
    # Verifica se o jogo chegou a um estado terminal (nenhum movimento válido)
    return len(getValidMoves(board, 'X')) == 0 and len(getValidMoves(board, 'O')) == 0


def evaluate(board, computerTile):
    # Função de avaliação para determinar o valor do tabuleiro para o jogador computador
    score = getScoreOfBoard(board)
    return score[computerTile]


def getOpponentTile(tile):
    # Retorna a peça do oponente dado uma peça atual
    return 'O' if tile == 'X' else 'X'


def showPoints(playerTile, computerTile):
    # Mostra o score atual
    scores = getScoreOfBoard(mainBoard)
    print('Player1: %s ponto(s). \nComputador: %s ponto(s).' %
          (scores[playerTile], scores[computerTile]))


print('Welcome to Reversi!')
while True:
    # Reseta o jogo e o tabuleiro
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    showHints = False
    turn = whoGoesFirst()
    print('O ' + turn + ' começa o jogo.')
    while True:
        if turn == 'player':
            # Player's turn.
            if showHints:
                validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            move = getPlayerMove(mainBoard, playerTile)
            if move == 'quit':
                print('Obrigado por jogar!')
                sys.exit()  # terminate the program
            elif move == 'hints':
                showHints = not showHints
                continue
            else:
                makeMove(mainBoard, playerTile, move[0], move[1])
            if getValidMoves(mainBoard, computerTile) == [] and getValidMoves(mainBoard, playerTile) == []:
                print('Não há jogadas válidas.')
                break
            elif getValidMoves(mainBoard, computerTile) == []:
                print('O computador não têm jogadas válidas.')
                turn = 'player'
            else:
                turn = 'computer'
        else:
            # Computer's turn.
            drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            input('Pressione Enter para ver a jogada do computador.')
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)
            if getValidMoves(mainBoard, computerTile) == [] and getValidMoves(mainBoard, playerTile) == []:
                print('Não há jogadas válidas.')
                break
            elif getValidMoves(mainBoard, playerTile) == []:
                print('O player não têm jogadas válidas.')
                turn = 'computer'
            else:
                turn = 'player'
    # Mostra o resultado final.
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print('X: %s ponto(s) \nO: %s ponto(s).' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('Você venceu o computador por %s ponto(s)! \nParabéns!' %
              (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('Você perdeu!\nO computador venceu você por %s ponto(s).' %
              (scores[computerTile] - scores[playerTile]))
    else:
        print('Empate!')
    if not playAgain():
        break
