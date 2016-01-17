# -*- coding: cp1252 -*-
# Itera��o (loops ou la�os)

# La�o for
#
# for <var controle> in <seq>:
#   <cmd1>
#   ...
#   <cmdn>
#
# Executa o bloco para cada elemento em <seq>, atribuindo
# cada elemento � vari�vel <var controle>

# O caractere c est� dentro da string s?
def contem(s, c):
    # Para cada caractere de s
    for car in s:
        if car == c:
            return True
    return False

# La�os com acumulador

# Quantas vezes c aparece em s?
def quantas_vezes(s, c):
    # acumulador
    a = 0
    for car in s:
        if car == c:
            a = a + 1
    return a

# Reimplementa str.find
# Acha a posi��o da primeira ocorr�ncia de c em s (se n�o achar retorna -1)
def strfind(s, c):
    # onde estou
    pos = -1
    for car in s:
        pos = pos + 1
        if car == c:
            # achei e est� em pos
            return pos
    # n�o achei
    return -1    

# Acha a posi��o da ultima ocorr�ncia de c em s (se n�o achar retorna -1)
def ultima(s, c):
    # onde estou
    pos = -1
    # posi��o da �ltima ocorr�ncia
    res = -1
    for car in s:
        pos = pos + 1
        if car == c:
            res = pos
    return res

# Fun��o construtora de sequ�ncias num�ricas: range
# range(n): 0, 1, ..., n-1 (intervalo [0,n))
def ultima2(s, c):
    # posi��o da �ltima ocorr�ncia
    res = -1
    for pos in range(len(s)):
        if s[pos] == c:
            res = pos
    return res

# range(n1, n2): n1, n1+1, ..., n2-1 (intervalo [n1,n2))
# acha primeira ocorr�ncia de c em s come�ando a partir do elemento n:
def strfind2(s, c, n):
    for pos in range(n, len(s)):
        if s[pos] == c:
            return pos
    return -1

def strfind3(s, c, n):
    pos = n    
    for car in s[n:len(s)]:
        if car == c:
            return pos
        pos = pos + 1
    return -1

# range(n1, n2, n3): n1, n1 + n3, ...,
#       (�ltimo n�mero que n�o ultrapassa ou iguala a n2)
# range(0, n, 1) � o mesmo que range(n)
# range(n1, n2, 1) � o mesmo que range(n1, n2)

# Soma dos n�meros �mpares menores que n:
def somaimp(n):
    soma = 0
    for x in range(1, n, 2):
        soma = soma + x
    return soma

def ultima3(s, c):
    for pos in range(len(s)-1, -1, -1):
        if s[pos] == c:
            return pos
    return -1

# Listas
# Sequ�ncias de elementos onde podemos acrescentar e remover elementos
# Em geral listas s�o homog�neas: os elementos t�m o mesmo tipo
# Constr�i-se uma lista de v�rias maneiras
# A mais simples � construir do mesmo modo que uma tupla, mas usando []
# ao inv�s de ()

L1 = [3, 9, 0, 4, 5, 7]
L2 = ["foo", "abc", "abracadabra", "ola mundo"]
# Lista heterog�nea
L3 = [42, True, "foo", (4, 5)]

# Opera��es
# Tamanho
# len(L1) == 6
# len(L2) == 4
# Indexa�ao
# L1[3] == 4
# L2[0] == "foo"
# L3[-1] == (4, 5)
# Fatiar
L4 = L1[2:5]
# L4 == [0, 4, 5]

# Soma uma lista de n�meros
def soma(l):
    s = 0
    for x in l:
        s = s + x
    return s

# As fun��es range retornam listas!

# N�meros �mpares menores que n
def impares(n):
    return range(1, n, 2)

def somaimp2(n):
    return soma(impares(n))
