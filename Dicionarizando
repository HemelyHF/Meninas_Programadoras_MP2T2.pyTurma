# -*- coding: utf-8 -*-
def adicionar(item): #MP2T2 Dicionarizando...
    cont = 1
    soma = ''
    
    while item != 'fim':
        sem = 0
        aforo = 0
        if cont > 1:
          soma = soma + ', '
        for i in item.split():
            if i.isnumeric():
                sem = i
            else:
                aforo = i
        febre = "'%s': %s" %(aforo,sem)
        soma = soma + febre
        cont += 1
        print('{' + soma + '}')
        item = input()
    return soma


leste = input()
adicionar(leste)
