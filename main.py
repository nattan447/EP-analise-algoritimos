import random
import matplotlib.pyplot as plt
# import numpy as np
from sys import platform
import time as T

import math






#n = 1000
#V =[random.randint(0,9999) for i in range(n)]

def mediaT(T, n):
        """     
        Esta função calcula a média de um vetor V

        Args :
        V   (list): O vetor que servira de base para a média.
        n(int): O numero de elementos do vetor

        Returns : int: A média dos n elementos do vetor
        """
        soma = 0
        for valor in T:
            soma += valor
        media = soma / n
        return media



#variancia
def varT(T,n):
    """
    Esta função calcula a variância do vetor V
    Args :
     V(list): O vetor que servira de base para a média.
     n(int): O numero de elementos do vetor
     
     Returns : 
     int: A  variação dos valores do vetor V    
    """
    media=mediaT(T,n) # retorna a média dos valores do vetor
    print("média "+ str(media))
    desvio = [] #vetor para guardar valores de desvio
    i = 0
    variacao = 0 # ira guardar o valor da variação
    while i<n:
        if media>T[i]:
            subtracao = media-T[i]
            desvio.append(subtracao)
        else:
            subtracao = T[i]-media
            desvio.append(subtracao)
        i+=1
    u = 0
    while u<n:
        variacao += (desvio[u]*desvio[u])/n# calcula a variacaO
        u+=1
    return variacao #retorna a variação



#selection sort
def selection(V,n):
    i = 0
    while i<n:
        u = i+1
        while u<n:
            menor = V[i]
            if V[i]>V[u]:
                V[i] = V[u]
                V[u] = menor
            u+=1
        i+=1

#bubble sort
def bubble(V, n):
    for i in range(n):
        trocou = False
        for j in range(n - 1):
            if V[j] > V[j + 1]:
                trocou = True
                # Troca os elementos de lugar se estiverem fora de ordem
                V[j], V[j + 1] = V[j + 1], V[j]
        if trocou==False:
            break
                        


#insertion
def insertion(V,n):
    i = 0
    while i<n-1:
        menor = V[i+1]
        if menor<V[i]:
            V[i+1] = V[i]
            V[i] = menor
            menor = V[i]
            u = i-1
            while u>=0:
                #quando um existir um elemento menor do que o menor de todos, a malha de repetiçaõ ira voltar para checar se existe um numenor menor ainda.
                menor = V[u+1]
                if V[u]>menor:
                    V[u+1] = V[u]
                    V[u] = menor
                    menor = V[u]
                u+= -1
        i+=1

def counting(V,n):
    i = 0
    count = 0
    maior = V[0]
    vetorFrequencia = []
    copiaV = [] #vetor que servira de copia de V para não ocorrer alterações indesejaveis em V no meio do algoritimo
    while i<n:
        if maior!= V[i] and  maior<V[i]:
            maior = V[i]
        copiaV.append(V[i])
        i+=1
    for i in range(maior):
       vetorFrequencia.append(0)
    for u in range(n):
        vetorFrequencia[copiaV[u]-1] += 1 # calcula a frequencia que cada elemento aparece
    for j in range(len(vetorFrequencia)-1):
        vetorFrequencia[j+1] += vetorFrequencia[j] # soma dos elementos vizinhos n1,n2 para obter quantos elementos n elementos são <=n2
    k = n-1
    while k>=0:
        indexelementofinal = vetorFrequencia[copiaV[k]-1] # index que o elemento copiav[k] deve ser posto
        vetorFrequencia[copiaV[k]-1] += -1
        V[indexelementofinal-1] = copiaV[k]
        k+= -1

def sortPy (V,n):
    V.sort()

contador = 0

def embaralha(V,n,p):
    
    if p>=1:
        print("comço a embaralha")
        quantidadePosicoes = (p*n)/100
        k = 1
        counter = 0 # counter vai servir para não permutar uma mesma posição
        iniciposicao = random.randint(0,n-1)
        inicivalor = V[iniciposicao]
        while k<=quantidadePosicoes:
            novaposicRamdom = random.randint(0,n-1)
            if V[iniciposicao]!=V[novaposicRamdom]:
                # print("permutou    "+str(V[iniciposicao]))
                # print("com    "+ str(V[novaposicRamdom]))
                V[iniciposicao] = V[novaposicRamdom]
                V[novaposicRamdom] = inicivalor
            else :
                # print("não permutou  " +str(V[iniciposicao]))
                # print("com    "+ str(V[novaposicRamdom]))

                # se der o mesmo valor não vão permutar
                # e vai rodar até permutar
                k+= -1
            #basicamente x permuta com algum y para cada iteração
            iniciposicao = random.randint(0,n-1)
            inicivalor = V[iniciposicao]
            k+=1
        print("cabo")
    # print(V)
                


def timeMe(func,V,n,m,p):
    w = 0
    global contador
    tempoarray = []
    while w<m :
        contador+=1
        vsorted = list(V)
        embaralha(vsorted,n,p)
        print(contador)
        start = T.process_time()
        func(vsorted,n)
        finish = T.process_time()
        tempoarray.append(finish-start)
        contador+=1
        print(contador)
    
        w+=1
    media = mediaT(tempoarray,m)
    variancia = varT(tempoarray,m)
    contador+=1
    print("contador         "+ str(contador))
    return media,variancia









#experimento 1
''''
def callalgorithims(V,n,p):
    print("porcentagem "+str(p))
    vsorted = list(V)
    resultado = timeMe(bubble,vsorted,n,10,p)
    bublemedia.append(resultado[0])
    desviopadrao = math.sqrt(resultado[1])
    bublevarianciamedia.append(desviopadrao)
    vsorted = list(V)
    resultado = timeMe(counting,vsorted,n,10,p)
    countingmedia.append(resultado[0])
    desviopadrao = math.sqrt(resultado[1])
    countingvariancia.append(desviopadrao)
    vsorted = list(V)
    resultado = timeMe(insertion,vsorted,n,10,p)
    insertionmedia.append(resultado[0])
    desviopadrao = math.sqrt(desviopadrao)
    insertionvariancia.append(resultado[1])
    vsorted = list(V)
    resultado = timeMe(selection,vsorted,n,10,p)
    seleciotnmedia.append(resultado[0])
    desviopadrao = math.sqrt(resultado[1])
    selectionvariancia.append(desviopadrao)
    vsorted = list(V)
    resultado = timeMe(sortPy,vsorted,n,10,p)
    sortpythonmedia.append(resultado[0])
    desviopadrao = math.sqrt(resultado[1])
    sortpythonvariancia.append(desviopadrao)
  





sortpythonmedia = []
sortpythonmedia = []
sortpythonvariancia = []
seleciotnmedia = []
selectionvariancia = []
insertionmedia = []
insertionvariancia =  []
countingmedia = [ ]
countingvariancia = []
bublemedia = []
bublevarianciamedia =  []
callalgorithims(V,n,0)
n= 5000
V = [random.randint(0,9999) for i in range(n)]
callalgorithims(V,n,0)





n = 10000
V = [random.randint(0,9999) for i in range(n)]
callalgorithims(V,n,0)


n = 50000

V = [random.randint(0,9999) for i in range(n)]
callalgorithims(V,n,0)


n = 100000

print("TA NOS CEM MIL")
V = [random.randint(0,9999) for i in range(n)]
callalgorithims(V,n,0)
'''

titulo = "grafico de tempo levado de ordenação para cada algoritimo"
xtitulo = "tamanhos"
nomegif = "exp1.png"
def GraficaSortings(mpontos, mediaMCMPi, desvioMCMPi):
    for i in range(len(mpontos)):
        xpontos = mpontos[i]
        ypontos = mediaMCMPi[i]
        desvios = desvioMCMPi[i]
        algoritimo = algoritmos[i]
        plt.errorbar(xpontos, ypontos, yerr=desvios, fmt='-o',label = algoritimo)
    plt.xlabel(xtitulo)
    plt.ylabel("tempo médio")
    plt.legend()
    plt.title(titulo)
    plt.savefig(nomegif)

    plt.show()
    plt.clf()
    print("Olá mundo")




#listamedias = [seleciotnmedia,bublemedia,countingmedia,insertionmedia,sortpythonmedia ]
#listadesviopadrao = [selectionvariancia,bublevarianciamedia,countingvariancia,insertionvariancia,sortpythonvariancia]
#lgoritmos = ['Selection', 'Bubble', 'Counting', 'Insertion','timsort']

#GraficaSortings([[1000,5000,10000,50000,100000],[1000,5000,10000,50000,100000],[1000,5000,10000,50000,100000],[1000,5000,10000,50000,100000],[1000,5000,10000,50000,100000]], listamedias, listadesviopadrao,)








#experimento 2

sortpythonmedia = []
sortpythonvariancia = []
insertionmedia = []
insertionvariancia =  []
bublemedia = []
bublevarianciamedia =  []

def callalgorithims2(V,n,p):
    print("porcentagem "+str(p))
    vsorted = list(V)
    resultado = timeMe(sortPy,vsorted,n,10,p)
    sortpythonmedia.append(resultado[0])
    desviopadrao = math.sqrt(resultado[1])
    sortpythonvariancia.append(desviopadrao)
    vsorted = list(V)
    resultado = timeMe(insertion,vsorted,n,10,p)
    insertionmedia.append(resultado[0])
    desviopadrao = math.sqrt(resultado[1])
    insertionvariancia.append(desviopadrao)
    vsorted = list(V)
    resultado = timeMe(bubble,vsorted,n,10,p)
    bublemedia.append(resultado[0])
    desviopadrao = math.sqrt(resultado[1])
    bublevarianciamedia.append(desviopadrao)
    
   



nomegif = "exp2.png"
titulo = "grafico de tempo levado de ordenação para cada algoritimo com p% desordenação"
xtitulo  ="porcentagem de desordenação"
n  = 100000
V = [random.randint(0,9999) for i in range(n)]
V.sort()
callalgorithims2(V,n,1)

callalgorithims2(V,n,3)

callalgorithims2(V,n,5)

callalgorithims2(V,n,10)

callalgorithims2(V,n,50)
listamedias = [bublemedia,insertionmedia,sortpythonmedia ]
print("lista medias "+ str(listamedias))
listadesviopadrao = [bublevarianciamedia,insertionvariancia,sortpythonvariancia]
print("desivo padrao"+str(listadesviopadrao))
algoritmos = [ 'Bubble', 'Insertion','timsort']
GraficaSortings([[1,3,5,10,50],[1,3,5,10,50],[1,3,5,10,50]], listamedias, listadesviopadrao,)











