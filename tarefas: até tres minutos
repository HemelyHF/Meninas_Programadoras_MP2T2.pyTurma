# -*- coding: utf-8 -*-
def inserir(arg, lista): #tarefas até três minutos
  lista.append(arg)
  return lista
 
valor = input()
resultado = ''
lista = []
while valor != '.':
  valor = valor.split(' ', 1)
  numero = int(valor[0])
  if numero <= 3:
    valor.pop(0)
    print('Fazer agora a tarefa:', valor.pop(0))
    valor = input()

  else:
    valor.pop(0)
    resultado = inserir(valor.pop(0), lista)
    lista = resultado
    valor = input()
print(lista)
