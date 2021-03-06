---
layout: default
title: Lab 3 de MAB 240
relpath: ..
---

MAB 240 - Computação II
=======================

Laboratório 3 - 11/05/2016
--------------------------

O objetivo deste laboratório é exercitar a criação de interfaces
e classes que as implementam. Vocês farão isso no contexto da
implementação de um *interpretador*, um programa que executa
programas.

As construções dos programas que vamos executar
serão modeladas como instâncias de classes, mas as construções
do programa se dividem em dois tipos mais abstratos, Expressões
e Comandos, que iremos modelar com interfaces. A implementação
dos métodos dessas interfaces se tornará a implementação do
interpretador.

MicroJava é uma linguagem de programação bem simples, mas
relativamente completa, onde pegamos um subconjunto de Java
contendo expressões aritméticas simples (soma, subtração,
multiplicação, divisão), variáveis e atribuição (mas sem declarações
e tipos; todas as variáveis são do tipo `double`), entrada e
saída simples através de comandos `readDouble` e `println`, testes
`if` e laços `while`. Por exemplo, o programa MicroJava
abaixo calcula o fatorial de um número pedido na entrada e o
mostra na saída:

{% highlight java %}
x = readDouble(); 
if(0 < x) {
  fact = 1;
  while(0 < x) { 
    fact = fact * x;
    x = x - 1;
  }
  println(fact);
}
{% endhighlight %}

Reparem que não é necessário declarar as variávieis `x` e `fact`, muito
menos declarar classes e métodos. Um programa MicroJava é simplesmente uma
sequência de comandos MicroJava.

Nesse laboratório vocês irão implementar classes que modelam a estrutura
de um programa MicroJava, e métodos para executar expressões e comandos MicroJava.
As estruturas de um programa MicroJava se dividem em dois grupos, expressões
e comandos, então comece definindo as interfaces `Expressao` e
`Comando`, inicialmente vazias. 

Agora vamos implementar as classes que modelam expressões. Todas elas devem
implementar a interface `Expressao`. Os campos de cada classe estão implícitos
na sua descrição. Não se esqueça de implementar um construtor também. As
classes são:

`Num` modela um numeral, e contém o valor do mesmo (um `double`). No programa
acima, 0 e 1 são instâncias de `Num`.  

`Var` modela uma variável, e contém o nome da variável. No programa acima, `x` e `fact`
são instâncias de `Var`.

`Soma`, `Sub`, `Mul` e `Div` modelam as quatro operações aritméticas, e
contêm duas expressões, para o lado esquerdo e o lado direito da
operação. No programa acima, `fact * x` é uma instância de `Mul` e `x - 1`
é uma instância de `Sub`.

`Igual` e `Menor` modelam as operações de comparação, e também contêm
expressões para o lado esquerdo e direito da operação. No programa acima, 
`0 < x` e `0 < fact` são instâncias de `Menor`.

`LeNumero` modela uma expressão de entrada, e não contém nennum campo.
No programa acima a `readDouble()` é uma instância de `LeNumero`.

Agora vocês irão adicionar um método
`double valor(java.util.HashMap<String, Double> vars)` à interface `Expressao`, 
e implementar esse método para
todas as classes acima. Nas operações de comparação `valor` deve
retornar 0 se a operação for falsa e 1 se for verdadeira, pois MicroJava
não possui valores booleanos. O mapa `vars` passado associa nomes de
variáveis aos seus valores. Se uma variável não está nesse mapa então seu
valor é 0.

As classes a seguir modelam os comandos. Todas elas implementam a
interface `Comando`. Implemente as classes, declarando seus campos
e seu construtor:

`Imprime` modela um comando de escrita, e contém a expressão cujo valor
será escrito. No programa acima, `println(fact);` é uma instância de `Imprime`.

`Atrib` modela um comando de atribuição, e contém o **nome** da variável a ser
atribuída e a expressão cujo valor será atribuído. No programa acima, 
`x = readDouble();`, `fact = 1;`, `fact = fact * x` e `x = x - 1` são todos
instâncias de `Atrib`.

`If` modela um comando `if/then/else`, e contém a expressão de teste e
dois comandos, um para a parte `then` e outro para a parte `else`. Tudo entre
a segunda e a última linhas no programa acima é uma instância de `If`.

`While` modela um comando `while`, e contém um comando para o
corpo do laço e uma expressão para a condição do laço. Tudo entre as linhas
4 e 7 do programa acima é uma instância de `While`.

`Bloco` modela uma sequência de comandos, e contém um vetor de comandos. 

O programa exemplo mostrado no início dessa página é uma instância de `Bloco`
com dois comandos,
uma atribuição e um `if`. O corpo do `If` é um bloco com três comandos, uma
atribuição, um `while` e um `println`, e o corpo do `while` é um bloco com
dois comandos, ambos de atribuição.

Finalmente, adicionem um método `void executa(java.util.HashMap<String, Double> vars)` à
interface `Comando`, e implementem esse método para todas as classes
acima. Usem a sua intuição e seus conhecimentos de programação para
pensar sobre como cada comando funciona. Novamente, `vars` é um mapa de nomes
de variáveis para seus valores.

****

Dica: o código abaixo irá te ajudar na implementação do método
`valor` da classe `LeNumero`:

{% highlight java %}
// Variável global para a entrada padrão
static java.util.Scanner STDIN = new java.util.Scanner(System.in);

// Função para ler um double da entrada padrão
public static double readDouble() {
  return STDIN.nextDouble();
}
{% endhighlight %}

O trecho de código a seguir instancia um programa MicroJava com a estrutura
do programa fatorial acima. Note como é passado um bloco vazio para o lado `else` do
`if`. Execute-o para ver o resultado:

{% highlight java %}
public class Fatorial {
  public static void main(String[] args) {
    Comando prog = 
      new Bloco(new Comando[] {
                  new Atrib("x", new LeNumero()),
                  new If(new Menor(new Num(0), new Var("x")),
                         new Bloco(new Comando[] {
                                     new Atrib("fat", new Num(1)),
                                     new While(new Menor(new Num(0), new Var("x")),
                                               new Bloco(new Comando[] { 
                                                           new Atrib("fat", new Mul(
                                                                              new Var("fat"),
                                                                              new Var("x"))),     
                                                           new Atrib("x", new Sub(new Var("x"),
                                                                                  new Num(1)))
                                               })),
                                     new Imprime(new Var("fat"))
                                   }),
                         new Bloco(new Comando[] { }))
                });
    prog.executa(new java.util.HashMap<String, Double>());
  }
}
{% endhighlight %}

O programa a seguir calcula a média final das três provas pelas
nossas regras de avaliação:

{% highlight java %}
public class MediaProvas {
  public static void main(String[] args) {
    /*
    * read p1;
    * read p2;
    * read p3;
    * if p1 < p2 then
    *   if p1 < p3 then
    *     write (p2 + p3) / 2
    *   else
    *     write (p1 + p2) / 2
    *   end
    * else
    *   if p2 < p3 then
    *     write (p1 + p3) / 2
    *   else
    *     write (p1 + p2) / 2
    *   end
    * end
    */
    Comando prog = new Bloco(new Comando[] { new Atrib("p1", new LeNumero()),
                                             new Atrib("p2", new LeNumero()),
                                             new Atrib("p3", new LeNumero()),
                                             new If(new Menor(new Var("p1"), new Var("p2")),
                                                    new If(new Menor(new Var("p1"), new Var("p3")),
                                                           new Imprime(new Div(new Soma(new Var("p2"),
                                                                                        new Var("p3")),
                                                                               new Num(2))),
                                                           new Imprime(new Div(new Soma(new Var("p1"),
                                                                                        new Var("p2")),
                                                                               new Num(2)))),
                                                    new If(new Menor(new Var("p2"), new Var("p3")),
                                                           new Imprime(new Div(new Soma(new Var("p1"),
                                                                                        new Var("p3")),
                                                                               new Num(2))),
                                                           new Imprime(new Div(new Soma(new Var("p1"),
                                                                                        new Var("p2")),
                                                                               new Num(2))))) });

    prog.executa(new java.util.HashMap<String, Double>());
  }
}
{% endhighlight %}

* * * * *

Última Atualização: {{ site.time | date: "%Y-%m-%d %H:%M" }}
