---
layout: default
title: Linguagens de Programação
relpath: ..
---

Linguagens de Programação
=========================

Apresentação
------------

Está é a página da disciplina Linguagens de Programação, do professor
Fabio Mascarenhas, para o semestre de 2013.1. As aulas da disciplina são
às segundas e quartas, das 13 às 15 horas, na sala DCC.

O objetivo dessa disciplina é expor os alunos aos diferentes paradigmas
de programação, mostrando a eles o que está "atrás da cortina" desses
paradigmas. Os alunos aprenderão como a maneira de funcionamento das 
linguagens com as quais eles já estão familizarizados é apenas uma possibilidade
em um grande espaço de linguagens possíveis. Para isso faremos tanto o
estudo de "linguagens símbolo" dos diferentes paradigmas, quanto a construção
e estudo de pequenos interpretadores para linguagens que são exemplos estilizados
dos mesmos paradigmas.

Os alunos precisam ter uma boa desenvoltura com programação, em especial com
estruturas de dados e funções recursivas. Não é necessário conhecimento da teoria
de linguagens formais, ou de técnicas de compilação; o enfoque desse curso é o 
comportamento das linguagens e não análise sintática ou geração de código.

Ementa
------

Introdução à programação funcional pura; programação funcional com
*Scala*: funções como valores, case classes, pattern matching; padrões de programação
funcional: listas, mapas e folds; o interpretador de *fun*, uma mini-linguagem funcional;
regras de escopo de seu efeito em funções de primeira classe; acrescentando tipos
a fun; o familiar revisitado: *microC*, uma linguagem imperativa com ponteiros
e funções de primeira ordem; lvalues vs. rvalues; programação OO destilada: a linguagem
*Smalltalk*; classes e metaclasses; um interpretador para Smalltalk.

Avaliação
---------

A avaliação será feita por provas e por pequenos trabalhos práticos. A
nota das provas corresponderá a 60% da nota final (6 pontos) e a dos
trabalhos a 40% (4 pontos). Serão três provas, uma na metade do período
e as outras duas no final, e será feita uma média aritmética das duas
maiores notas. Não haverá prova final ou segunda chamada. A média
final é 5,0.

Lista de Discussão
------------------

Temos um grupo no Facebook para perguntas e avisos sobre a matéria.
Acessem [aqui](https://www.facebook.com/groups/lpufrj).

Livros
------

Não existe um livro texto único para essa disciplina. O que mais se aproxima disso é
o [Programming Languages: Application and Interpretation](http://cs.brown.edu/~sk/Publications/Books/ProgLangs/),
de Shriram Krishnamurthi, por adotar a estratégia de explicar conceitos de linguagens
de programação através do estudo de pequenos interpretadores. Outro livro que adota
a mesma estratégia é o [Essentials of Programming Languages](http://www.eopl3.com/), de
Friedman e Wand. 

Os livros acima usam [Racket](http://racket-lang.org/) como linguagem
de implementação dos seus interpretadores, enquanto vamos usar [Scala](http://www.scala-lang.org/),
que tem uma sintaxe mais familiar para programadores C e Java. O curso de
[programação funcional com Scala](https://www.coursera.org/course/progfun) do criador
da linguagem, Martin Odersky, é um bom tutorial para o subconjunto de Scala que
vamos usar.

Provavelmente o melhor livro para uma visão de alto nível dos conceitos de linguagens de
programação é o [Programming Language Pragmatics](http://www.cs.rochester.edu/~scott/pragmatics/), de
Michael Scott. É uma boa referência para resumos de vários temas que serão cobertos em sala.

Contato
-------

Podem entrar em contato pelo meu [email](mailto:mascarenhas@ufrj.br) que
responderei assim que possível. Também tenho um horário de atendimento
de alunos na minha sala, segundas e quartas de 17 às 18 horas. A sala é
a E-2013 do DCC.

* * * * *

Última Atualização: {{ site.time | date: "%Y-%m-%d %H:%M" }}