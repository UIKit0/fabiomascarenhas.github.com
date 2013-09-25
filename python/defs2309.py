# -*- coding: cp1252 -*-

# Quebra uma string em duas partes
# str int -> str str
# Partes antes e depois da posi��o n
# n�o incluir o caractere na posi��o n
def quebra_strn(s, n):
    return s[0:n], s[n+1:len(s)]

# Quebra uma string em duas partes
# str str -> str str
# Partes antes e depois da primeira ocorr�ncia de c
# n�o incluir o caractere c
def quebra_strc(s, c):
    n = str.find(s, c) 
    return quebra_strn(s, n)

# Quebra uma string em duas partes
# str int -> str str
# str str -> str str
def quebra_str(s, x):
    if type(x) == int:
        return quebra_strn(s, x)
    else: # x � uma str
        return quebra_strc(s, x)

# Quebra uma string em duas partes
# str str -> str str
# Partes antes e depois da primeira ocorr�ncia de c
# n�o incluir o caractere c, e ignorar diferen�a
# entre mai�sculas e min�sculas
# resposta deve respeitar mai�sculas/min�sculas da
# cadeia original
def quebra_stri(s, c):
    n = str.find(str.upper(s), str.upper(c))
    return quebra_strn(s, n)   

# Substitui < por &lt; r > por &gt; na cadeia
# str -> str
def escape(s):
    s1 = str.replace(s, ">", "&gt;")
    s2 = str.replace(s1, "<", "&lt;")
    return s2    # str.replace(str.replace(s, ">", "&gt;"), "<", "&lt;")


# Uma cor � uma tripla de valores float no intervalo [0.0,1.0]
BRANCO = (1.0, 1.0, 1.0)
PRETO = (0.0, 0.0, 0.0)
VERMELHO = (1.0, 0.0, 0.0)
VERDE = (0.0, 1.0, 0.0)
AZUL = (0.0, 0.0, 1.0)

# Complemento de uma cor
# cor -> cor
def complemento(cor):
    return (1.0 - cor[0], 1.0 - cor[1], 1.0 - cor[2])

# M�ximo entre dois n�meros
# num num -> num
def max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

def max3(n1, n2, n3):
    return max(max(n1, n2), n3)

# Soma de cores (m�ximo de cada compomente)
# cor cor -> cor
def soma(c1, c2):
    return (max(c1[0], c2[0]), max(c1[1], c2[1]), max(c1[2], c2[2]))

# M�dia aritm�tica entre dois n�meros
# num num -> float
def median(n1, n2):
    return (n1 + n2) / 2.0

# M�dia de cores (m�dia de cada componente)
# cor cor -> cor
def media(c1, c2):
    return (median(c1[0], c2[0]), median(c1[1], c2[1]), median(c1[2], c2[2]))

# Registro de um aluno � um dicion�rio com tr�s componentes (ou campos)
# "nome" -> nome do aluno (uma str)
# "dre" -> DRE do aluno (uma str)
# "notas" -> tripla de notas (uma tripla de floats)
# "faltas" -> quantas faltas (um int)
JOAO = { "nome": "Jo�o", "dre": "123456789", "notas": (5.0, 3.5, 8.3), "faltas": 4 }
MARIA = { "nome": "Maria", "dre": "234567890", "notas": (5.0, 3.5, 4.0), "faltas": 4 }
FABIO = { "nome": "Jo�o", "dre": "345678901", "notas": (4.0, 3.5, 3.7), "faltas": 10 }
ZENOBIO = { "nome": "Jo�o", "dre": "456789012", "notas": (4.0, 3.5, 10.0), "faltas": 10 }

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

# D� os dois maiores de tr�s floats
# float float float -> float float
def dois_maiores(f1, f2, f3):
    min, med, max = ordena3(f1, f2, f3)
    return max, med

# M�dia aritm�tica dois dois maiores de tr�s floats
# float float float -> float
def media_maiores(f1, f2, f3):
    return median(*dois_maiores(f1, f2, f3))

# Aluno aprovado ou n�o, e de que jeito
# aluno -> str
def aprovado(aluno):
    media = media_maiores(*aluno["notas"])
    faltas = aluno["faltas"]
    if media >= 5.0 and faltas <= 7:
        return "AP"
    elif media < 5.0 and faltas > 7:
        return "RFM"
    elif media < 5.0:
        return "RM"
    else:
        return "RF"

# Um registro de aprova��o � um dicion�rio com um �nico componente
# O nome desse componente � o DRE de algum aluno, e seu valor uma dupla
# com o nome do aluno e sua condi��o de aprova��o (uma dupla de str)

# A partir do aluno retorna um dicion�rio com seu registro
# de aprova��o
# aluno -> ra
def ra(aluno):
    return { aluno["dre"]: (aluno["nome"], aprovado(aluno)) }

# O estado do jogo de forca � um dicion�rio com os campos (ou componentes):
# "palavra": palavra pra ser advinhada (uma str de tamanho 4)
# "mascara": quais foram os acertos (qu�drupla de bools)
# "erros": quantos foram os erros (um int)
JOGO = { "palavra": "abra", "mascara": (False, False, False, False), "erros": 0 }

# "soma" duas qu�druplas de booleanos fazendo o ou l�gico de cada componente
# mascara mascara -> mascara
def soma_mascara(m1, m2):
    return (m1[0] or m2[0], m1[1] or m2[1], m1[2] or m2[2], m1[3] or m2[3])

# diz se a m�scara est� completa (todos os elementos True) ou n�o
# mascara -> bool
def mascara_completa(m):
    return m[0] and m[1] and m[2] and m[3]

# Em que posi��es a letra aparece na palavra
# str str -> mascara
def tentativa(palavra, letra):
    return (palavra[0] == letra, palavra[1] == letra, palavra[2] == letra, palavra[3] == letra)

# Uma rodada do jogo, ou atualiza a mascara ou o n�mero de erros
# estado str -> estado
def rodada(estado, letra):
    m = tentativa(estado["palavra"], letra)
    nova_mascara = soma_mascara(estado["mascara"], m)
    if nova_mascara != estado["mascara"]:
        return { "palavra": estado["palavra"],
                 "mascara": nova_mascara,
                 "erros": estado["erros"] }
    else:
        return { "palavra": estado["palavra"],
                 "mascara": estado["mascara"],
                 "erros": estado["erros"] + 1 }

# Uma rodada do jogo, testando se acabou ou n�o
# estado str -> "GANHOU"
# estado str -> "PERDEU"
# estado str -> estado
def rodada_final(estado, letra):
    novo_estado = rodada(estado, letra)
    if mascara_completa(novo_estado["mascara"]):
        return "GANHOU"
    elif novo_estado["erros"] == 6:
        return "PERDEU"
    else:
        return novo_estado
