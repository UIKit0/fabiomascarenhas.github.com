import Tkinter
import math

def cor_tkinter(cor):
    return "#%02x%02x%02x" % (int(cor[0]*255),
                              int(cor[1]*255),
                              int(cor[2]*255))

class Janela(Tkinter.Tk):
    def __init__(self, titulo, larg, alt):
        Tkinter.Tk.__init__(self)
        self.title(titulo)
        x = (self.winfo_screenwidth()-larg)/2
        y = (self.winfo_screenheight()-alt)/2
        self.geometry("%dx%d+%d+%d" % (larg, alt, x, y))
        self.resizable(False, False)
        #self["bg"] = "#ffffff"
        self.componentes()

    def componentes(self):
        raise NotImplementedError()

class Botao(Tkinter.Button):
    def __init__(self, janela, x, y, larg, alt, texto, tamanho):
        Tkinter.Button.__init__(self, janela)
        self["text"] = texto
        self["font"] = "Arial %d" % tamanho
        self.place({ "x": x, "y": y, 
                     "width": larg, "height": alt })
        self["command"] = self.executar

    def executar(self):
        raise NotImplementedError()

class Canvas(Tkinter.Canvas):
    def __init__(self, janela, x, y, larg, alt):
        Tkinter.Canvas.__init__(self, janela)
        self["bg"] = "#ffffff"
        self.bind("<ButtonPress-1>", self.apertou)
        self.bind("<ButtonRelease-1>", self.soltou)
        self.bind("<B1-Motion>", self.arrastou)
        self.place({ "x": x, "y": y, "width": larg, "height": alt })

    def apertou(self, evt):
        pass

    def soltou(self, evt):
        pass

    def arrastou(self, evt):
        pass

    def limpar(self):
        self.delete(Tkinter.ALL)

    def triangulo(self, p1, p2, p3, cor):
        self.create_polygon([p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]],
                            { "fill": cor_tkinter(cor), "outline": cor_tkinter(cor) })

    def linha(self, p1, p2, cor):
        self.create_line(p1[0], p1[1], p2[0], p2[1],
                         { "fill": cor_tkinter(cor) })

class CaixaTexto(Tkinter.Text):
    def __init__(self, janela, x, y, larg, alt, tamanho):
        Tkinter.Text.__init__(self, janela)
        self["font"] = "Arial %d" % tamanho
        self.place({ "x": x, "y": y, "width": larg, "height": alt })

    def texto(self):
        return self.get(1.0, Tkinter.END)    

####
#### MODELO
####

class Tartaruga:
    def __init__(self):
        self.triangulo = [(-10, -7), (-10, 7), (10, 0)]
        self.obs = []
        self.reset()

    def reset(self):
        self.direcao = 0
        self.pos = (300, 300)
        self.escreve = True
        self.pontos = []
        self.notificar()
        
    def ponto(self, i):
        sd = math.sin(self.direcao)
        cd = math.cos(self.direcao)
        p = self.triangulo[i]
        return (p[0]*cd - p[1]*sd + self.pos[0],
                p[1]*cd + p[0]*sd + self.pos[1])

    def observar(self, o):
        self.obs.append(o)

    def notificar(self):
        for o in self.obs:
            o.mudou(self)

    def frente(self, dist):
        if self.escreve: self.pontos.append(self.pos)
        try:
            dx = dist * math.cos(self.direcao)
            dy = dist * math.sin(self.direcao)
            raise Exception("bug")
            self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        finally:
            if self.escreve: self.pontos.append(self.pos)
        self.notificar()

    def tras(self, dist):
        if self.escreve: self.pontos.append(self.pos)
        dx = dist * math.cos(self.direcao)
        dy = dist * math.sin(self.direcao)
        self.pos = (self.pos[0] - dx, self.pos[1] - dy)
        if self.escreve: self.pontos.append(self.pos)
        self.notificar()

    def esquerda(self, ang):
        self.direcao = self.direcao - ang * math.pi/180
        self.notificar()

    def direita(self, ang):
        self.direcao = self.direcao + ang * math.pi/180
        self.notificar()

    def levanta(self):
        self.escreve = False

    def abaixa(self):
        self.escreve = True

    def desenhar(self, canvas):
        for i in range(0, len(self.pontos)-1, 2):
            canvas.linha(self.pontos[i], self.pontos[i+1], (0, 0, 0))
        canvas.triangulo(self.ponto(0), self.ponto(1), self.ponto(2), (0, 0, 0))

####
#### Interface
####

class JanelaTartaruga(Janela):
    def __init__(self):
        Janela.__init__(self, "Tartaruga", 800, 600)        

    def componentes(self):
        modelo = Tartaruga()
        caixa = CaixaTexto(self, 600, 0, 200, 500, 16)
        BotaoExecutar(self, modelo, caixa)
        BotaoLimpar(self, modelo)
        self.canvas = Canvas(self, 0, 0, 600, 600)
        modelo.observar(self)
        modelo.reset()

    def mudou(self, modelo):
        self.canvas.limpar()
        modelo.desenhar(self.canvas)

class Observador:
    def __init__(self, canvas):
        self.canvas = canvas

    def mudou(self, modelo):
        self.canvas.limpar()
        modelo.desenhar(self.canvas)

class BotaoExecutar(Botao):
    def __init__(self, janela, modelo, caixa):
        Botao.__init__(self, janela, 600, 500, 200, 50, "Executar", 16)
        self.modelo = modelo
        self.caixa = caixa

    def interpretar(self, linha):
        espaco = linha.find(" ")
        if espaco != -1:
            comando = linha[0:espaco]
            argumento = int(linha[espaco+1:])
            if comando == "frente":
                self.modelo.frente(argumento)
            elif comando == "tras":
                self.modelo.tras(argumento)
            elif comando == "esquerda":
                self.modelo.esquerda(argumento)
            elif comando == "direita":
                self.modelo.direita(argumento)
            else:
                raise NameError(comando)
        else:
            if linha == "levanta":
                self.modelo.levanta()
            elif linha == "abaixa":
                self.modelo.abaixa()
            elif linha != "":
                raise NameError(linha)
        
    def executar(self):
        texto = self.caixa.texto()
        for linha in texto.splitlines():
            try:
                self.interpretar(linha)
            except ValueError:
                print "argumento invalido"
            except NameError as erro:
                print "comando %s invalido" % erro.message 
            except Exception as erro:
                print "outro problema: %s" % erro.message

class BotaoLimpar(Botao):
    def __init__(self, janela, modelo):
        Botao.__init__(self, janela, 600, 550, 200, 50, "Limpar", 16)
        self.modelo = modelo
    
    def executar(self):
        self.modelo.reset()

#### Rodando
        
raiz = JanelaTartaruga()
raiz.mainloop()