import random 
n = 50
V =[random.randint(0,9999) for i in range(n)]
vsorted = list(V)
# vsorted.sort() #ordena o vetor vsorted
def mediaV(V,n):
    """
    Esta função calcula a média de um vetor V
    
    Args :
    V(list): O vetor que servira de base para a média.
    n(int): O numero de elementos do vetor

    Returns : int: A média dos n elementos do vetor
    """
    
    u = 0
    soma = 0
    while u<n:
        soma += V[u]
        u+=1
    return soma/n 


#variancia 
def varV(V,n):
    """
    Esta função calcula a variância do vetor V
    Args :
     V(list): O vetor que servira de base para a média.
     n(int): O numero de elementos do vetor
     
     Returns : 
     int: A  variação dos valores do vetor V    
    """
    media=mediaV(V,n) # retorna a média dos valores do vetor
    print("média "+ str(media))
    desvio = [] #vetor para guardar valores de variação
    i = 0
    variacao = 0 # ira guardar o valor da variação
    while i<n:
        if media>V[i]:
            subtracao = media-V[i]
            desvio.append(subtracao)
        else:
            subtracao = V[i]-media
            desvio.append(subtracao)
        i+=1
    u = 0
    while u<n:
        variacao += (desvio[u]*desvio[u])/n# calcula o desvio padrão
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
def bubble(V,n):
    i = 0
    while i<n:
        u = 0
        while u<n-1:
            maior = V[u+1]
            if V[u]>maior:
                #coloca o elemento maior na frente do menor, para cada comparação de 2 a 2
                V[u+1]= V[u]
                V[u] = maior
            u+=1
        i+=1


#insertion
def insetion(V,n):
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

insetion(V,n)
print(V)




