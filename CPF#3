# -*- coding: utf-8 -*-
numero = input()                   # CPF 3
numero = numero.replace('.', '')
numero = numero.replace('-', '')

quantidade = False
contagem = len(numero) # length
tudonumero = False

for something in numero:
  if something in '1234567890':
    tudonumero = True

  else:
    tudonumero = False

if tudonumero == False:
  print('ENCODING ERROR')

if contagem == 11:
  quantidade = True
else:
  print('SIZE ERROR')

if quantidade == True and tudonumero == True:
  print(numero)
