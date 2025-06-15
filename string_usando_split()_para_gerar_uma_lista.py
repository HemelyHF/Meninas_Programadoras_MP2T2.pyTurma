# -*- coding: utf-8 -*-
linha = input() #string: usando split() para gerar uma lista
contador = 0

l_strings = []
for s in linha.split():
  l_strings.append(s)
  contador += 1
l_inteiros = []
for i in linha.split():
  i = int(i)
  dobra = i * 2
  l_inteiros.append(dobra)

l_decimais = []
for f in linha.split():
  f = float(f)
  divide = f / 2
  l_decimais.append(divide)

print(l_strings)
print(l_inteiros)
print(l_decimais)
print(contador)
