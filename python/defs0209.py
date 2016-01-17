# -*- coding: cp1252 -*-

import math

# Quantos bombons posso comprar
# n�mero n�mero -> int
def qtd_bombons_dec(dinheiro, preco):
    return int(dinheiro / preco)

# Qual o troco da compra
# n�mero n�mer -> n�mero
def troco_bombons_dec(dinheiro, preco):
    return dinheiro % preco

# Quantos bombons e qual o troco
# n�mero n�mero -> int n�mero
def bombons_dec(dinheiro, preco):
    return qtd_bombons_dec(dinheiro, preco), troco_bombons_dec(dinheiro, preco)

# Quantos bombons posso comprar
# int int -> int
def qtd_bombons_int(dinheiro, preco):
    return dinheiro / preco

def troco_bombons_dec(dinheiro, preco):
    return dinheiro % preco

# Quantos bombons e qual o troco
# Valores em reais
# n�mero n�mero -> int n�mero
def bombons_int(dinheiro, preco):
    dinheiro_cent = int(dinheiro * 100)
    preco_cent = int(preco * 100)
    return qtd_bombons_int(dinheiro, preco), troco_bombons_int(dinheiro, preco) / 100.0

# Hipotenusa dados os catetos
# n�mero n�mero -> float
def hipotenusa(b, c):
    return math.sqrt(b * b + c * c)

# Perimetro dados os catetos
# n�mero n�mero -> float
def perimetro(b, c):
    return b + c + hipotenusa(b, c)

# Solu��es reais de uma eq. de 2o. grau
# Entrada: coeficientes
# Saida: n�mero de solu��es e solu��es
# n�mero n�mero n�mero -> 2 float float
# n�mero n�mero n�mero -> 1 float
# n�mero n�mero n�mero -> 0
def raizes(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return 0
    elif delta == 0:
        return 1, -b / (2.0 * a)
    else:
        rdelta = math.sqrt(delta)
        doisa = 2.0 * a
        menosb = -b
        return 2, (menosb + rdelta) / doisa, (menosb - rdelta) / doisa 
