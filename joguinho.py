import keyboard
import os

PAREDES = "*"

NUM_LINHA = 10
NUM_COLUNA = 10


#calcular meio da matriz
if NUM_LINHA%2 != 0:
    meio_linha = (NUM_LINHA + 1)/2
else:
    meio_linha = NUM_LINHA / 2

if NUM_COLUNA%2 != 0:
    meio_coluna = (NUM_COLUNA + 1)/2
else:
    meio_coluna = NUM_COLUNA/2

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
                    if direcao != "" and i == ultima_posicao_i and j == ultima_posicao_j:
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


def andar(direcao, posicao_i, posicao_j):
    retorno = 0

    if direcao == "i":
        ultima_posicao_i = posicao_i
        ultima_posicao_j = posicao_j
        retorno = criaMatriz(direcao, ultima_posicao_i, ultima_posicao_j)
        desenhaMatriz()
        matriz.clear()

    if direcao == "w":
        ultima_posicao_i = posicao_i - 1
        ultima_posicao_j = posicao_j
        retorno = criaMatriz(direcao, ultima_posicao_i, ultima_posicao_j)
        desenhaMatriz()
        matriz.clear()

    if direcao == "s":
        ultima_posicao_i = posicao_i + 1
        ultima_posicao_j = posicao_j
        retorno = criaMatriz(direcao, ultima_posicao_i, ultima_posicao_j)
        desenhaMatriz()
        matriz.clear()
    
    if direcao == "a":
        ultima_posicao_i = posicao_i
        ultima_posicao_j = posicao_j - 1
        retorno = criaMatriz(direcao, ultima_posicao_i, ultima_posicao_j)
        desenhaMatriz()
        matriz.clear()

    if direcao == "d":
        ultima_posicao_i = posicao_i
        ultima_posicao_j = posicao_j + 1
        retorno = criaMatriz(direcao, ultima_posicao_i, ultima_posicao_j)
        desenhaMatriz()
        matriz.clear()
    return retorno
    
print("APERTE ESC PARA FINALIZAR")
print("INICIO\n")
retorno = andar("i",meio_coluna,meio_linha)
print(retorno)
while(True):
    
    if keyboard.is_pressed('w'):
        os.system('cls')
        print("APERTE ESC PARA FINALIZAR")
        print("ANDEI PRA CIMA\n")
        retorno = andar("w",retorno[0],retorno[1])
        print(retorno)
    if keyboard.is_pressed('s'):
        os.system('cls')
        print("APERTE ESC PARA FINALIZAR")
        print("ANDEI PRA BAIXO\n")
        retorno = andar("s",retorno[0],retorno[1])
        print(retorno)
    if keyboard.is_pressed('a'):
        os.system('cls')
        print("APERTE ESC PARA FINALIZAR")
        print("ANDEI PRA ESQUERDA\n")
        retorno = andar("a",retorno[0],retorno[1])
        print(retorno)
    if keyboard.is_pressed('d'):
        os.system('cls')
        print("APERTE ESC PARA FINALIZAR")
        print("ANDEI PRA DIREITA\n")
        retorno = andar("d",retorno[0],retorno[1])
        print(retorno)
    
    if keyboard.is_pressed('esc'):
        print("JOGO FINALIZADO")
        os.system('pause')
        break
