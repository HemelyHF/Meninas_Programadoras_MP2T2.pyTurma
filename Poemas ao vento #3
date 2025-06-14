# -*- coding: utf-8 -*-
comeco = input() #palavras ao vento #1 e 2
comeco = comeco.lower()
dicionario = {}
substituir = [',', '.', '"', "'"]

for tipo in substituir:
  comeco = comeco.replace(tipo, '')

lista = comeco.split()

for palavra in lista:
  if palavra in dicionario:
    dicionario[palavra] += 1

  else:
    dicionario[palavra] = 1

print(dicionario)

novo = input()



while novo != '.':
    novo = novo.lower()
  
    if novo in comeco:
    #print(dicionario)
      print(dicionario[novo])
      novo = input()

    else:
    #print(dicionario)
      print(novo, "não encontrada")
      novo = input()
