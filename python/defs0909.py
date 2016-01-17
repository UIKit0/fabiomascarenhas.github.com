# -*- coding: cp1252 -*-

# Quest�o 10 Lab 2

"""
Fa�a uma fun��o que receba tr�s valores e os retorne em ordem
crescente. Fa�a uma fun��o que receba tr�s valores e retorne
o terceiro deles. Fa�a uma terceira fun��o que comp�e as
duas anteriores para fazer uma fun��o que recebe tr�s valores
e retorna o maior deles.
"""
# Ordena��o de tr�s valores
# Funciona com qualquer tipo de valor que eu possa comparar!
def ordena3(a, b, c):
    if a < b:
        if b < c: # a < b < c
            return a, b, c
        else:
            if a < c: # a < c < b
                return a, c, b
            else: # c < a < b
                return c, a, b
    else:
        if c < b: # c < b < a.
            return c, b, a
        else:
            if a < c: # b < a < c
                return b, a, c
            else: # b < c < a
                return b, c, a

# Menor de dois
def min2(a, b):
    if a < b:
        return a
    else:
        return b
            
# Menor de tr�s
def min3(a, b, c):
    return min2(min2(a, b), c)

# Maior de dois
def max2(a, b):
    if a < b:
        return b
    else:
        return a

# Maior de tr�s
def max3(a, b, c):
    return max2(max2(a, b), c)

# Ordena��o de tr�s n�meros
def ordena3num(a, b, c):
    menor = min3(a, b, c)
    maior = max3(a, b, c)
    meio = a + b + c - menor - maior
    return menor, meio, maior

# Complemento de uma cor dada por uma tripla de n�meros em [0.0, 1.0]
def complemento1(cor):
    return (1.0 - cor[0], 1.0 - cor[1], 1.0 - cor[2])

def complemento2(cor):
    vermelho, verde, azul = cor
    return (1.0 - vermelho, 1.0 - verde, 1.0 - azul)


# Dicion�rios

# Criar um dicion�rio
# { ... campos ... }
# campo: "nome do campo": valor

azul = { 'azul': 1.0, 'vermelho': 0.0, 'verde': 0.0 }

# Complemento de uma cor dada por um dicion�rio
def complemento_dict(cor):
    return { 'azul': 1.0 - cor['azul'],
             'verde': 1.0 - cor['verde'],
             'vermelho': 1.0 - cor['vermelho'] }

comp_azul = complemento_dict(azul)

# Estado e tempo

contador = 0   # contador � uma vari�vel global

# incremento e decremento
def inc():
    global contador   # quero usar o contador definido no corpo principal
    contador = contador + 1
    return contador

def dec():
    global contador
    contador = contador - 1
    return contador

def inc10():
    inc()
    inc()
    inc()
    inc()
    inc()
    inc()
    inc()
    inc()
    inc()
    inc()


