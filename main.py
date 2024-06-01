import random
import matplotlib.pyplot as plt
# import numpy as np
from sys import platform
import time as T








n = 10
V =[random.randint(0,9999) for i in range(n)]

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
def varT(T, n):
    media = mediaT(T, n)
    soma_diferencas_quadradas = 0
    for valor in T:
        soma_diferencas_quadradas += (valor - media) ** 2
    variancia = soma_diferencas_quadradas / n
    return variancia



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
def bubble(V,n):
    i = 0
    while i<n:
        u = 0
        while u<n-1:
            maior = V[u+1]
            if V[u]>V[u+1]:
                #coloca o elemento maior na frente do menor, para cada comparação de 2 a 2
                V[u+1]= V[u]
                V[u] = maior
            u+=1
        i+=1


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


def embaralha(V,n,p):
    if p>=1:
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
    # print(V)
                

contador = 0

def timeMe(func,V,n,m,p):
    w = 0
    global contador
    tempoarray = []
    while w<m :
        vsorted = list(V)
        embaralha(vsorted,n,p)
        start = T.process_time()
        func(V,n)
        finish = T.process_time()
        tempoarray.append(finish-start)
    
        w+=1
    media = mediaT(tempoarray,m)
    variancia = varT(tempoarray,m)
    contador+=1
    print(contador)
    return media,variancia






#experimento 1
def callalgorithims(V,n,p):
    print("porcentagem "+str(p))
    vsorted = list(V)
    resultado = timeMe(bubble,vsorted,n,10,p)
    bublemedia.append(resultado[0])
    bublevarianciamedia.append(resultado[1])
    vsorted = list(V)
    resultado = timeMe(counting,vsorted,n,10,p)
    countingmedia.append(resultado[0])
    countingvariancia.append(resultado[1])
    vsorted = list(V)
    resultado = timeMe(insertion,vsorted,n,10,p)
    insertionmedia.append(resultado[0])
    insertionvariancia.append(resultado[1])
    vsorted = list(V)
    resultado = timeMe(selection,vsorted,n,10,p)
    seleciotnmedia.append(resultado[0])
    selectionvariancia.append(resultado[1])
    vsorted = list(V)
    resultado = timeMe(sortPy,vsorted,n,10,p)
    sortpythonmedia.append(resultado[0])
    sortpythonvariancia.append(resultado[1])
  





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
n= 50
V = [random.randint(0,9999) for i in range(n)]
callalgorithims(V,n,0)





n = 100
V = [random.randint(0,9999) for i in range(n)]
callalgorithims(V,n,0)


n = 500

V = [random.randint(0,9999) for i in range(n)]
callalgorithims(V,n,0)


n = 1000

print("TA NOS CEM MIL")
V = [random.randint(0,9999) for i in range(n)]
callalgorithims(V,n,0)


titulo = "grafico de tempo levado de ordenação para cada algoritimo"
xtitulo = "tamanhos"

def GraficaSortings(mpontos, mediaMCMPi, desvioMCMPi):
    for media, desvio ,algoritimo in zip(mediaMCMPi, desvioMCMPi,algoritmos):
        plt.errorbar(mpontos, media, yerr=desvio, fmt='o-',label = algoritimo)
    plt.xlabel(xtitulo)
    plt.ylabel("tempo(s)")
    plt.legend()
    plt.title(titulo)
    plt.show()
    plt.clf()
    print("Olá mundo")




listamedias = [seleciotnmedia,bublemedia,countingmedia,insertionmedia,sortpythonmedia ]
listavariancias = [selectionvariancia,bublevarianciamedia,countingvariancia,insertionvariancia,sortpythonvariancia]
algoritmos = ['Selection', 'Bubble', 'Counting', 'Insertion','sort']

GraficaSortings([1000, 5000, 10000, 50000,100000], listamedias, listavariancias,)








#experimento 2






# sortpythonmedia = []
# sortpythonmedia = []
# sortpythonvariancia = []
# seleciotnmedia = []
# selectionvariancia = []
# insertionmedia = []
# insertionvariancia =  []
# countingmedia = [ ]
# countingvariancia = []
# bublemedia = []
# bublevarianciamedia =  []



# titulo = "grafico de tempo levado de ordenação para cada algoritimo com p% desordenação"
# xtitulo  ="porcentagem de desordenação"
# n  = 100000
# V =[i for i in range(n)]
# callalgorithims(V,n,1)
# callalgorithims(V,n,3)
# callalgorithims(V,n,5)
# callalgorithims(V,n,10)
# callalgorithims(V,n,50)
# listamedias = [bublemedia,insertionmedia,sortpythonmedia ]
# listavariancias = [bublevarianciamedia,insertionvariancia,sortpythonvariancia]
# algoritmos = [ 'Bubble', 'Insertion','sortpython']
# GraficaSortings([1, 3, 5, 10,50], listamedias, listavariancias,)










