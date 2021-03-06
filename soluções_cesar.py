# -*- coding: utf-8 -*-
"""Soluções Cesar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f9iSsVGRDvFiG38kuREY080QL3259sUK

**1. Substituindo caracteres no local:**

Example:

Input: “User is not allowed “, 19

Output: “User&32is&32not&32allowed”
"""

s='User is not allowed' 
s.replace(" ", "&32")

"""**2. Verifique as palavras com letras desordenadas:**
Considere permutação parcial apenas se:
- A primeira letra não mudou de lugar
- Se a palavra tiver mais de 3 letras, até 2/3 das letras mudaram de lugar

2A - Checando se ambas palavras iniciam com mesma letra:
"""

def check_inicial (str1, str2):#Mesma inicial
  if (str1[0] == str2[0]):
    return True

str1='probably'
str2='porbalby'
str1=str1.upper()
str2=str2.upper()
print(f'******Checando se {str2} possui mesma inicial de {str1}:********')
print('---------------------------')
iniciais = check_inicial(str1,str2)

if iniciais==True: 
  print('Ambas palavras iniciam com a mesma letra - OK')
else:
    print('Palavras não iniciam com a mesma letra - Não OK')

"""2B. Checando se as palavras possuem mesmo tamanho:"""

def check_tam(str1, str2):
  if (len(str1) == len(str2)):#Tam iguais
      return True
str1='probably'
str2='porbalby'
str1=str1.upper()
str2=str2.upper()
print(f'******Checando se {str2} é de mesmo tamanho de {str1}:********')
print('---------------------------')

tamanho = check_tam(str1, str2)

if tamanho==True: 
  print('Palavras possuem mesmo tamanho - OK')
else:
  print('As Palavras não são do mesmo tamanho - Não OK')

"""2C. Se as letras de uma palavra coincidem na outra:"""

def check_coincide(str1,str2):#Letras coincidem
    for letter in str2:
      if letter in str1:
        return True

str1='probably'
str2='porbalby'
str1=str1.upper()
str2=str2.upper()
print(f'******Checando se as letras de {str2} coincidem em {str1}:********')
print('---------------------------')

coincide = check_coincide(str1, str2)

if coincide==True:
  print(f'As letras de {str2} aparecem em {str1}- OK')
else: 
  print(f'Nem todas as letras de {str2} aparecem em {str1}- Não OK')

"""2D. Checando se a palavra chave é formada somente de letras:"""

str1='probably'
str2='porbalby'
str1=str1.upper()
str2=str2.upper()
print(f'******Checando se {str2} é formado por letras somente:********')
print('---------------------------')
#Saber se só tem letras      
if (str2.isalpha()):
  print(f'A palavra : {str2} é formada somente por letras')
else:
  print(f'A palavra : {str2} não possui somente letras')

"""2E. Checando a similaridade entre as palavras com difflib"""

import difflib
str1='pale'
str2='ple'
s = difflib.SequenceMatcher(None, str1, str2)#passando as strings para o diffilib
s.find_longest_match(0,len(str1),0,len(str2))#retornando a quantidade de caracteres semelhantes
print('A similaridade entre as palavras é de: ',round(difflib.SequenceMatcher(None, str1, str2).ratio(),2),'%')#retornando o índice de similaridade

"""2F. Checando se a chave informada é um anagrama da 1ª palavra:"""

def anagramas(str1):
  if len(str1)<=1:
    return str1
  else:
    tmp=[]
    for aux in anagramas(str1[1:]):
            for i in range(len(str1)):
                tmp.append(aux[:i] + str1[0:1] + aux[i:])
    return tmp

str1='probably'
str2='porbalby'
str1=str1.upper()
str2=str2.upper()
print(f'******Checando se {str2} é um anagrama de {str1}:********')
print('---------------------------')
lista = anagramas(str1)
if(str2 in lista): #busca a incidência na lista de anagramas
  print(f'{str2} é um anagrama de {str1}')
else:
  print(f'{str2} não é um anagrama de {str1}')

"""**3. Verifique palavras com erros de digitação:** 

Dadas duas strings, escreva uma função para verificar se elas estão com um erro de digitação (ou com zero erros).

Exemplos:

pale, ple ¬> true
"""

from difflib import SequenceMatcher
def similar (str2, str1):
  return SequenceMatcher(None, str2, str1).ratio() 
str1='pale'
str2='ple'
str1=str1.upper()
str2=str2.upper()
a=similar (str2, str1)
arred=round(a,2)
if (arred==1.0):
  print(f'{str2} é igual à chave {str1}')
elif (arred<1.0):
  print(f'{str2} têm de chance de ser um erro de digitação')