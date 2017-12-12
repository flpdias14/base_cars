#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from math import sqrt




# Método para carregar um arquivo
def loadFile(arquivo, lim):
    # abre o arquivo
    f = open(arquivo)
    # le as linhas do arquivo
    linhas = f.readlines()
    lista = []
    returnList = []
    try:
        for linha in linhas:
            # separa e faz o cast nos valores
            lista = linha.split(",")
            lista[6] = lista[6].replace('\n', '')
            returnList.append(lista)
            lista = []
    except:
        # print '--- fim da leitura do arquivo ' + file + " .---"
        pass
    return returnList



def id(att1, att2):
    # print "Distancia entre "+att1+" e "+att2+": "
    if len(att1) == len(att2):
        soma = sum(caratere1 != caratere2 for caratere1, caratere2 in zip(att1, att2))
        # print soma
        return soma


    else: return 1000000

def distanciaHamming(elementoTreino, elementoTeste):
    soma = id(elementoTreino[0], elementoTeste[0])
    # soma += id(elementoTreino[1], elementoTeste[1])
    # soma += id(elementoTreino[2], elementoTeste[2])
    # soma += id(elementoTreino[3], elementoTeste[3])
    # soma += id(elementoTreino[4], elementoTeste[4])
    # soma += id(elementoTreino[5], elementoTeste[5])
    # assert len(elementoTreino[0]) == len(elementoTreino[0])
    # assert len(elementoTreino[1]) == len(elementoTreino[1])
    # soma = sum(ch1 != ch2 for ch1, ch2 in zip(elementoTreino[0], elementoTeste[0]))
    # # soma += sum(ch1 != ch2 for ch1, ch2 in zip(elementoTreino[1], elementoTeste[1]))
    # assert len(elementoTreino[2]) == len(elementoTreino[2])
    # soma += sum(ch1 != ch2 for ch1, ch2 in zip(elementoTreino[2], elementoTeste[2]))
    # assert len(elementoTreino[3]) == len(elementoTreino[3])
    # soma += sum(ch1 != ch2 for ch1, ch2 in zip(elementoTreino[3], elementoTeste[3]))
    # assert len(elementoTreino[4]) == len(elementoTreino[4])
    # soma += sum(ch1 != ch2 for ch1, ch2 in zip(elementoTreino[4], elementoTeste[4]))
    # assert len(elementoTreino[5]) == len(elementoTreino[5])
    # soma += sum(ch1 != ch2 for ch1, ch2 in zip(elementoTreino[5], elementoTeste[5]))
    return soma


# Método que calcula a distancia euclidiana entre os indivíduos
def calcDistEuclides(individuo1, individuo2):
    y = 2
    soma = pow(individuo1[0] - individuo2[0], y) + pow(individuo1[1] - individuo2[1], y) + pow(individuo1[2] - individuo2[2], y) + pow(individuo1[3] - individuo2[3], y)
    return sqrt(soma)

# Método para classificar um indivíduo, retorna a classe a que o indivíduo pertence
def classificar(treino, individuo, k=1, peso=False):
    # declaração da lista de distancias
    distancias = []

    # declara a variável de retorno
    classificacao = ""
#     calcula as distancias com base nos casos de treino
    for i in treino:
        dist = []
        dist.append(distanciaHamming(i, individuo))
        # guarda a classe para não se perder na ordenação
        dist.append(i[6])
        distancias.append(dist)
#     ordena os valores
    distancias.sort(cmp=None, key=None, reverse=False)
#     verifica os valores de k
    if k == 1:
        classificacao = distancias[0][1]
    else:
        if peso:
            # Declara listas com labels para contagem de cada classe
            unacc = [0.0, 'unacc']
            acc = [0.0,'acc']
            good = [0.0,'good']
            vgood = [0.0, 'vgood']
            # percorre os k vizinhos
            for i in range(k):
                # verifica se pertence a classe unnac
                if unacc[1] == distancias[i][1]:
    #               incrementa o contador de setosa
                    if  distancias[i][0] != 0:
                        unacc[0] +=1/distancias[i][0]
                    else:
                        unacc[0] += 1000
                # verifica se pertence a classe acc
                elif acc[1] == distancias[i][1]:
                    # incrementa o contador de versicolor
                    if distancias[i][0] != 0:
                        acc[0] +=1/ distancias[i][0]
                    else:
                        acc[0] +=1000
                # verifica e incremena , caso good
                elif good[1] == distancias[i][1]:
                    if distancias[i][0] != 0:
                        good[0] +=1/distancias[i][0]
                    else:
                        good[0] += 1000
                #verifica e incrementa, caso v-good
                elif vgood[1] == distancias[i][1]:
                    if distancias[i][0] != 0:
                        vgood[0] +=1/distancias[i][0]
                    else:
                        vgood[0] += 1000

            # rank para ordenar as classes
            rank = []
            rank.append(unacc)
            rank.append(acc)
            rank.append(good)
            rank.append(vgood)
            # ordena do menor para o maior
            rank.sort(cmp=None, key=None, reverse=False)
            print rank
            # print rank # pega o maior valor
            classificacao = rank[-1][1]
        else:
            # Declara listas com labels para contagem de cada classe
            unacc = [0.0, 'unacc']
            acc = [0.0,'acc']
            good = [0.0,'good']
            vgood = [0.0, 'vgood']

            # percorre os k vizinhos
            for i in range(k):

                # verifica se pertence a classe setosa
                if unnac[1] == distancias[i][1]:
    #               incrementa o contador de setosa
                    unnac[0] +=1
                # verifica se pertence a classe versicolor
                elif acc[1] == distancias[i][1]:
                    # incrementa o contador de versicolor
                    acc[0] +=1
    #                 verifica e incremena , caso virginica
                elif good[1] == distancias[i][1]:
                    good[0] +=1
                elif vgood[1] == distancias[i][1]:
                    vgood[0] +=1

            # rank para ordenar as classes
            rank = []
            rank.append(unnac)
            rank.append(acc)
            rank.append(good)
            rank.append(vgood)
            # ordena do menor para o maior
            rank.sort(cmp=None, key=None, reverse=False)
            # pega o maior valor
            classificacao = rank[-1][1]
    # print classificacao
    return classificacao


# Método que gera a matriz de confusão
def matrizConfusao(listaClassificada, listaClasses):
    # declaração da matriz
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in listaClassificada:
#         verifica se a classificação foi correta
        if i[4] == i[5]:
#             recupera o indice e adiciona na diagonal
            j = listaClasses.index(i[4])
            matriz[j][j] += 1
        else:
            # pega o indice da linha
            l = listaClasses.index(i[4])
            # pega o indice da coluna
            c = listaClasses.index(i[5])
            matriz[l][c] += 1
    return matriz
# carrega o arquivo de treino e classificação
# listaTreino = loadFile('iris-treino.txt', ',')
# listaClassificar = loadFile('iris-teste.txt', ',')

listaDados = loadFile('cars.txt', ',')

listaUnnac = []
listaAcc = []
listaGood = []
listaVGood = []

listaTreino = []
listaClassificar = []
# Separa as classes
for a in listaDados:
    if(a[6] == 'unnac'):
        listaUnnac.append(a)
    elif(a[6] == 'acc'):
        listaAcc.append(a)
    elif(a[6] == 'good') :
        listaGood.append(a)
    else:
        listaVGood.append(a)


listaTreinos = []
listaTestes = []
numUnnac = []
numAcc = []
numGood = []
numVGood = []

def sorteiaListaNumeros(quantidadeNum,rangeNum):
    lista = []
    num = 0
    for i in range(quantidadeNum):
        control = True
        while(control):
            num = randint(0, rangeNum)
            if(lista.count(num) == 0):
                lista.append(num)
                control = False
    return lista
lenUnnac = len(listaUnnac)
lenAcc = len(listaAcc)
lenGood = len(listaGood)
lenVGood = len(listaVGood)
for i in xrange(10):
    numSorteados = sorteiaListaNumeros(lenUnnac/2, lenUnnac-1)
    for j in numSorteados:
        listaTreino.append(listaUnnac[j])
    for j in xrange(lenUnnac):
        if numSorteados.count(j) == 0:
            listaClassificar.append(listaUnnac[j])
    numSorteados = sorteiaListaNumeros(lenAcc/2, lenAcc-1)
    for j in numSorteados:
        listaTreino.append(listaAcc[j])
    for j in xrange(lenAcc):
        if numSorteados.count(j) == 0:
            listaClassificar.append(listaAcc[j])
    numSorteados = sorteiaListaNumeros(lenGood/2, lenGood-1)
    for j in numSorteados:
        listaTreino.append(listaGood[j])
    for j in xrange(lenGood):
        if numSorteados.count(j) == 0:
            listaClassificar.append(listaGood[j])
    numSorteados = sorteiaListaNumeros(lenVGood/2, lenVGood-1)
    for j in numSorteados:
        listaTreino.append(listaVGood[j])
    for j in range(lenVGood):
        if numSorteados.count(j) == 0:
            listaClassificar.append(listaVGood[j])
    # print "Lista Treino : "
    # print len(listaTreino)
    # print "Lista Teste : "
    # print len(listaClassificar)
    listaTreinos.append(listaTreino)
    listaTestes.append(listaClassificar)
    listaTreino = []
    listaClassificar = []

# declaração da lista de individuos classificados
listaClassificada = []
listaClassificados = []
# Classifica os individuos

for i in range(10):
    # print len(listaTestes[i])
    for individuo in listaTestes[i]:

        p = classificar(listaTreinos[i], individuo, k=1, peso=True)
        if len(individuo) == 7:
            individuo.insert(7, p)
        #print p
        listaClassificada.append(individuo)
    listaClassificados.append(listaClassificada)
    listaClassificada = []

# print listaClassificados[i]

# for individuo in listaClassificar:
#     p = classificar(listaTreino, individuo, k=50, peso=False)
#     individuo.insert(5, p)
#     listaClassificada.append(individuo)



def somaLista(lista):
    total = 0
    for num in lista:
        total += num
    return total

def media(lista):
    soma = somaLista(lista)
    media = soma / float(len(lista))
    return media

def variancia(lista):
    media1 = media(lista)
    variancia = 0
    for num in lista:
        variancia += pow((media1 - num), 2.0)
    variancia = variancia / float(len(lista))
    return variancia

def std(variancia):
    return pow(variancia, (0.5))


# contadores de acertos e erros gerais
acertos = 0
erros = 0

classes = []
# contador de acertos das classes
ac1 = 0
ac2 = 0
ac3 = 0
# contador de erros das classes
ec1 = 0
ec2 = 0
ec3 = 0

listaAcertos = []
listaErros = []

for i in range(10):
    for individuo in listaClassificados[i]:
        # print individuo
        # print individuo
        if individuo[6] == individuo[7]:
            acertos += 1
        else:
            erros += 1
    listaAcertos.append(acertos)
    listaErros.append(erros)
    acertos = 0
    erros = 0

somaErros = 0
somaAcertos = 0

listaTaxasErro = []
listaTaxasAcerto = []
for i in range(10):
    listaTaxasErro.append((listaErros[i]/float((listaErros[i]+listaAcertos[i]))))

for i in range(10):
    listaTaxasAcerto.append(1-listaTaxasErro[i])


# for i in range(100):
    # print "Acerto teste "+str(i)+": "+str(listaAcertos[i])+ " Erro :"+str(listaErros[i])

print "Media Acertos: " + str(media(listaAcertos))
print "Media Erros: "+str(media(listaErros))
print "Variancia Acertos: "+str(variancia(listaAcertos))
print "Variancia Erros: "+str(variancia(listaErros))
print "Desvio Padrão Acertos: "+ str(std(variancia(listaAcertos)))
print "Desvio Padrão Erros: "+ str(std(variancia(listaErros)))
print "-----------------------------------------------------------"
print "Média taxas Acerto: "+str(media(listaTaxasAcerto)*100)+"%"
print "Média taxas Erro: "+str(media(listaTaxasErro)*100)+"%"
print "Desvio Padrão Taxa Acerto: "+str(std(variancia(listaTaxasAcerto)))
print "Desvio Padrão Taxa Erro: "+str(std(variancia(listaTaxasErro)))


#
# for individuo in listaClassificada:
#     # Separa uma lista com classes
#     if classes.count(individuo[4]) == 0:
#
#         classes.append(individuo[4])
# # Conta erros e acertos de classificação
# for individuo in listaClassificada:
#     # Verifica se a Classificação foi correta
#     if individuo[4] == individuo[5]:
#         # incrementa contador geral de acertos
#         acertos += 1
#         # incrementa contador de acertos da classe
#         if(individuo[5] == classes[0]):
#             ac1 += 1
#         elif (individuo[5] == classes[1]):
#             ac2 += 1
#         else:
#             ac3 += 1
#     else:
#
#         erros += 1
#         if(individuo[5] == classes[0]):
#             ec1 += 1
#         elif individuo[5] == classes[1]:
#             ec2 += 1
#         else:
#             ec3 += 1

# Calcula Erro de Classificação
# err = float(erros) / (erros + acertos)
# # Calcula o erro da classe
# errClasse1 = float(ec1) / (ac1 + ec1)
# errClasse2 = float(ec2) / (ac2 + ec2)
# errClasse3 = float(ec3) / (ac3 + ec3)

# Gera matriz confusão
# matriz = matrizConfusao(listaClassificada, classes)

# print "Acertos : " + str(acertos)
# print "Erros : " + str(erros)
# print "Taxa de Acerto: " + str(1-err)
# print "Taxa de Erro de Classificação : " + str(err)

#
# print "Erro Classe " + classes[0] + " : " + str(errClasse1)
# print "Erro Classe " + classes[1] + " : " + str(errClasse2)
# print "Erro Classe " + classes[2] + " :" + str(errClasse3)

#print "Matriz Confusão:"
#print "| %d %d %d |" % (matriz[0][0], matriz[0][1], matriz[0][2])
#print "| %d %d %d |" % (matriz[1][0], matriz[1][1], matriz[1][2])
#print "| %d %d %d |" % (matriz[2][0], matriz[2][1], matriz[2][2])
