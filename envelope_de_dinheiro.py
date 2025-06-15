# -*- coding: utf-8 -*-
def maximo(arg): #memoria utilizada
  adicao = 0 
  max = 0

  while arg != 0: #0 encerra o loop
    adicao = adicao + arg

    if max < adicao: #determina o max
      max = adicao
      arg = int(input())

    else:
      arg = int(input()) #proximo valor

  return  max

print(maximo(int(input())))
