# -*- coding: utf-8 -*-
valor = int(input())  #Balanço Financeiro Categorizado
positivo = 0
negativo = 0 

salario = 0
alimentacao = 0
moradia = 0
transporte = 0
saude = 0
lazer = 0
prestacao = 0


for something in range(valor):
  entrada = float(input())
  local = input()

  if entrada > 0:
    positivo = positivo + entrada

    if local == 'S':
      salario = salario + entrada

    elif local == 'P':
      prestacao = prestacao + entrada

  elif entrada < 0:
    negativo = negativo + entrada

    if local == 'A':
      alimentacao = alimentacao + entrada

    elif local == 'M':
      moradia = moradia + entrada

    elif local == 'T':
      transporte = transporte + entrada

    elif local == 'S':
      saude = saude + entrada

    elif local == 'L':
      lazer = lazer + entrada

soma = negativo + positivo

print("Movimentações")

if alimentacao != 0:
  print("  Alimentação:", '%.2f' % alimentacao)
if moradia != 0:
  print("  Moradia:", '%.2f' % moradia)
if transporte !=0:
  print("  Transporte:", '%.2f' % transporte)
if saude != 0:
  print("  Saúde:", '%.2f' % saude)
if lazer != 0:
  print("  Lazer:", '%.2f' % lazer)
if salario != 0:
  print("  Salário:", '%.2f' % salario)
if prestacao != 0:
  print("  Prestação de serviços:", '%.2f' % prestacao)

print("Total de Renda:", '%.2f' % positivo)
print("Total de Gastos:", '%.2f' % negativo)
print("Balanço:", '%.2f' % soma)
