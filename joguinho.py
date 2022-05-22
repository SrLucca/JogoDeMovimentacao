import keyboard
import os

PAREDES = "*"

NUM_LINHA = 5
NUM_COLUNA = 5

matriz = []

def criaMatriz(direcao, posicao_i, posicao_j):
    ultima_posicao_i = posicao_i
    ultima_posicao_j = posicao_j

    posicoes = [0,0]
    for i in range(NUM_LINHA):
        linha = []
        for j in range(NUM_COLUNA):
            if i == 0:
                linha.append(PAREDES)
            elif j == 0:
                linha.append(PAREDES)
            else:
                if i == NUM_LINHA-1:
                    linha.append(PAREDES)
                elif j == NUM_COLUNA-1:
                    linha.append(PAREDES)
                else:
                    if direcao == '' and i == 2 and j == 2:
                        linha.append('o')
                        ultima_posicao_i = i
                        ultima_posicao_j = j
                    elif direcao == 'w' and i == ultima_posicao_i - 1 and j == ultima_posicao_j:
                        linha.append('o')
                        ultima_posicao_i = i
                        ultima_posicao_j = j
                    elif direcao == 's' and i == ultima_posicao_i and j == ultima_posicao_j -1:
                        linha.append('o')
                        ultima_posicao_i = i
                        ultima_posicao_j = j
                    else:
                        linha.append(' ')
        matriz.append(linha)
        posicoes[0] = ultima_posicao_i
        posicoes[1] = ultima_posicao_j
    return posicoes

def desenhaMatriz():
    for elementos in matriz:
        print(' '.join(elementos))
    return matriz


direcao = ''
retorno = criaMatriz(direcao,2,2)
desenhaMatriz()
print(f"{retorno}")

while(True):
    


    if keyboard.is_pressed('w'):
        direcao = 'w'
        retorno = criaMatriz(direcao,retorno[0], retorno[1])
        desenhaMatriz()
        print(retorno)
    if keyboard.is_pressed('s'):
        direcao = 's'
        criaMatriz(direcao,retorno[0], retorno[1])
        desenhaMatriz()
        print(retorno)
    if keyboard.is_pressed('d'):
        direcao = 'd'
        criaMatriz(direcao,retorno[0], retorno[1])
        desenhaMatriz()
        print(retorno)
    if keyboard.is_pressed('a'):
        direcao = 'a'
        criaMatriz(direcao,retorno[0], retorno[1])
        desenhaMatriz()
        print(retorno)


