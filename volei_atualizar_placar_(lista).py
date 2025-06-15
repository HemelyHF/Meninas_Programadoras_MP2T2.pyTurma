# -*- coding: utf-8 -*-
time1 = input() #Volei: lista
time2 = input()
dado = [int(item) for item in input().split()]
ponto = 0
point = 0

tamanho = len(dado)
if dado[2] == 2:
  dado[1] = dado[1] + 1
  print(time1, dado[0])
  print(time2, dado[1])

elif dado[2] == 1:
  dado[0] = dado[0] + 1
  print(time1, dado[0])
  print(time2, dado[1])
