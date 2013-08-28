# -*- coding: cp1252 -*-

import math

# Calcula a �rea de um c�rculo
# n�mero -> float
# area_circulo(1) = 3.141592...
# area_circulo(2) = 12.56...
# area_circulo(3) = 28...
def area_circulo(raio):
    return math.pi * (raio ** 2)

# Calcula a �rea de uma coroa circular
# Par�metros: raio externo e raio interno
# n�mero n�mero -> float
# area_coroa(2, 1) = 9...
# area_coroa(3, 2) = 15...
def area_coroa(raioe, raioi):
    return area_circulo(raioe) - area_circulo(raioi)

# Converte hora, minuto e segundo em segundos
# Par�metros: hora, minuto, segundo
# int int int -> int
# segundos(1, 2, 30) = 3750
# segundos(0, 5, 0) = 300
# segundos(2, 0, 15) = 7215
def segundos(h, m, s):
    return h * 3600 + m * 60 + s

# Calcula o tempo de prova de um corredor em segundos
# Par�metros: hora, minuto e segundo de partida e hora, minuto e segundo
# de chegada
# int int int int int int -> int
# tempo_prova(1, 2, 30, 2, 2, 30) = 3600
# tempo_prova(1, 2, 30, 2, 1, 0) = 3510
# tempo_prova(1, 2, 30, 1, 20, 45) = 1095
def tempo_prova(hs, ms, ss, hc, mc, sc):
    return segundos(hc, mc, sc) - segundos(hs, ms, ss)

# Divis�o e resto
# Par�metros: dividendo e divisor
# int int -> int int
# divr(5, 2) = 2, 1
# divr(11, 3) = 3, 2
def divr(a, b):
    return a/b, a%b

# Converte segundos em horas, minutos e segundos
# int -> int int int
# hms(3600) = 1, 0, 0
# hms(300) = 0, 5, 0
# hms(7215) = 2, 0, 15
def hms(s):
    hora, resto = divr(s, 3600)
    minuto, segundo = divr(resto, 60)
    return hora, minuto, segundo

# Calcula o tempo de prova de um corredor em hora, min, seg
# Par�metros: hora, minuto e segundo de partida e hora, minuto e segundo
# de chegada
# int int int int int int -> int
# tempo_prova_hms(1, 2, 30, 2, 2, 30) = 1, 0, 0
# tempo_prova_hms(1, 2, 30, 2, 1, 0) = 0, 52, 30
# tempo_prova_hms(1, 2, 30, 1, 20, 45) = 0, 18, 15
def tempo_prova_hms(hs, ms, ss, hc, mc, sc):
    return hms(segundos(hc, mc, sc) - segundos(hs, ms, ss))


# Valor absoluto
# n�mero -> n�mero
# abs(5) = 5
# abs(-3) = 3
# abs(0) = 0
def abs(x):
    # Estrutura condicional
    if x >= 0:   # express�o condicional
        return x
    else:
        return -x

def abs2(x):
    # Estrutura condicional
    if x >= 0:   # express�o condicional
        return x
    elif x < 0:
        return -x
    
def f(x):
    if x > 3:
        return x
    elif x < -1:
        return -x
    else:
        return 1


def f2(x):
    if x > 3:
        return x
    elif (-1 <= x) and (x <= 3): # and � o conectivo l�gico "e" 
        return 1
    elif x < -1:
        return -x


