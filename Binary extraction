# -*- coding: utf-8 -*-
def lista(arg):      #MP2T2 Binary extraction
    leste = []
    for item in arg.split():
       item = int(item)
       leste.append(item)
    print(leste)
    return leste

def extrair(leste, meio):
    comprimento = len(leste)
    valor = int(input())
    novalista = []
   
    if valor <= comprimento:
        cont = 0
        while valor != len(novalista):
            if comprimento % 2 == 0: #par
                novalista.append(leste[meio + cont])
                if valor != len(novalista):
                        cont += 1
                        novalista.append(leste[meio - cont])

            elif comprimento % 2 != 0: #impar
                if cont == 0:
                    novalista.append(leste[meio])
                    cont += 1
                else:
                    novalista.append(leste[meio + cont])
                    if valor != len(novalista):
                        novalista.append(leste[meio - cont])
                        cont += 1

        print(novalista)
            
numero = lista(input())

metade = len(numero)/2
metade = int(metade)

extrair(numero, metade)
