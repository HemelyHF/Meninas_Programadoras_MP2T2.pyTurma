# -*- coding: utf-8 -*-
def lista(leste):        # Arrumação importante
    novalista = []
    for item in leste.split():
        item = int(item)
        novalista.append(item)
    print(novalista)
    print(novalista) #duas vezes
    return novalista

def metade(arg):
    leste = []
    for item in range(5):
        leste.append(arg[item])
    print(leste)
    return leste

def metade2(arg):
    leste = []
    for item in range(4):
        leste.append(arg[item])
    print(leste)
    return leste

def metade3(arg):
    leste = []
    for item in range(6):
        leste.append(arg[item])
    print(leste)
    return leste

def dosa(arg):
    leste = []
    for item in range(2):
        leste.append(arg[item])
    print(leste)
    return arg

def uno(arg):
    for item in range(2):
        leste = []
        leste.append(arg[item])
        print(leste)
    return arg

def tresa(arg):
    cont = 0
    leste = []
    arg.pop(0)
    arg.pop(0)
    print(arg)
    for item in range(3):
        if cont == 1:
          leste.append(arg[item])
        else:
            leste.append(arg[item])
            print(leste)
            leste = []
            cont = 1
    print(leste)
    return leste

def tresa2(arg):
    cont = 0
    leste = []
    leste.append(arg[0])
    leste.append(arg[1])
    leste.append(arg[2])
    print(leste)
    leste = []

    for item in range(3):
        if cont == 1:
          leste.append(arg[item])
        else:
            leste.append(arg[item])
            print(leste)
            leste = []
            cont = 1

    print(leste)
    return leste

def apaga(leste, tam):
    for item in range(tam):
        leste.pop(0)
    return leste

def sort(valor):
    leste = []
    for item in valor.split():
        item = int(item)
        leste.append(item)
    leste.sort()
    if len(leste) == 9:
        for item in range(9):
            leste[item] = str(leste[item])
        print('[' + leste[0] + ', ' + leste[1] + ', ' + leste[2] + ', ' + leste[3] + ', ' + leste[4] + ', ' + leste[5] + ', ' + leste[6] + ', ' + leste[7] + ', ' + leste[8] + ']')
    elif len(leste) == 10:
        for item in range(10):
            leste[item] = str(leste[item])
        print('[' + leste[0] + ', ' + leste[1] + ', ' + leste[2] + ', ' + leste[3] + ', ' + leste[4] + ', ' + leste[5] + ', ' + leste[6] + ', ' + leste[7] + ', ' + leste[8] + ', ' + leste[9] + ']')
    elif len(leste) == 11:
        for item in range(11):
            leste[item] = str(leste[item])
        print('[' + leste[0] + ', ' + leste[1] + ', ' + leste[2] + ', ' + leste[3] + ', ' + leste[4] + ', ' + leste[5] + ', ' + leste[6] + ', ' + leste[7] + ', ' + leste[8] + ', ' + leste[9] + ', ' + leste[10] + ']')
    elif len(leste) == 12:
        for item in range(12):
            leste[item] = str(leste[item])
        print('[' + leste[0] + ', ' + leste[1] + ', ' + leste[2] + ', ' + leste[3] + ', ' + leste[4] + ', ' + leste[5] + ', ' + leste[6] + ', ' + leste[7] + ', ' + leste[8] + ', ' + leste[9] + ', ' + leste[10] + ', ' + leste[11] + ']')
    elif len(leste) == 13:
        for item in range(13):
            leste[item] = str(leste[item])
        print('[' + leste[0] + ', ' + leste[1] + ', ' + leste[2] + ', ' + leste[3] + ', ' + leste[4] + ', ' + leste[5] + ', ' + leste[6] + ', ' + leste[7] + ', ' + leste[8] + ', ' + leste[9] + ', ' + leste[10] + ', ' + leste[11] + ', ' + leste[12] + ']')
    elif len(leste) == 14:
        for item in range(14):
            leste[item] = str(leste[item])
        print('[' + leste[0] + ', ' + leste[1] + ', ' + leste[2] + ', ' + leste[3] + ', ' + leste[4] + ', ' + leste[5] + ', ' + leste[6] + ', ' + leste[7] + ', ' + leste[8] + ', ' + leste[9] + ', ' + leste[10] + ', ' + leste[11] + ', ' + leste[12] + ', ' + leste[13] + ']')
    elif len(leste) == 15:
        for item in range(15):
            leste[item] = str(leste[item])
        print('[' + leste[0] + ', ' + leste[1] + ', ' + leste[2] + ', ' + leste[3] + ', ' + leste[4] + ', ' + leste[5] + ', ' + leste[6] + ', ' + leste[7] + ', ' + leste[8] + ', ' + leste[9] + ', ' + leste[10] + ', ' + leste[11] + ', ' + leste[12] + ', ' + leste[13] + ', ' + leste[14] +']')
    return leste

nemo = input()
liste = lista(nemo)
if len(liste) == 10:
  dir = metade(liste)
  elo = (dosa(dir))
  uno(elo)
  uno(tresa(elo))
  esq = apaga(liste, 5)
  print(esq)
  uno(tresa(uno(dosa(esq))))

elif len(liste) == 13:
  dir = metade3(liste)
  uno(tresa2(dir))
  dir.pop(0)
  uno(tresa(dir))
  esq = apaga(liste, 6)
  print(esq)
  uno(tresa2(esq))
  esq = apaga(esq, 3)
  print(esq)
  uno(dosa(esq))
  apaga(esq, 2)
  uno(dosa(esq))

elif (len(liste) == 9) or (len(liste) == 11) or (len(liste) == 12) or (len(liste) == 14) or (len(liste) == 15):
  dir = metade2(liste)
  uno(dosa(apaga(uno(dosa(dir)), 2)))
  esq = apaga(liste, 4)
  print(esq)
  uno(tresa(uno(dosa(esq))))

sort(nemo)
