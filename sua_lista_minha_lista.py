# -*- coding: utf-8 -*-
#MP2T2 Sua lista, minha lista
def menor(arg, lista2):
  liste = []
  for item in arg.split():
    item = int(item)
    liste.append(item)
  print('-', liste)
  print('+', lista2)

  while liste != []:
      menor = 10000
      for i in liste:
        if i < menor:
          menor = i
      liste.pop(liste.index(menor))
      lista2.append(menor)
      print('-', liste)
      print('+', lista2)

novalista = []
lista = input()
menor(lista, novalista)
