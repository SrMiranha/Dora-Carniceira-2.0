from tkinter import *
import tkinter as tk
 
 #COLOCAR A VACA E OS ESPINHOS
class Animal:#superclasse
    def __init__ (self,nome,força,posição_x,posição_y):#atributos
        self.nome=str(nome)  #O nome em maiusculo é o nome da variavel (atributo)
        self.força=int(força)
        self.posição_x=int(posição_x)
        self.posição_y=int(posição_y)

    def setforça(self,forçamudou):
        self.força=forçamudou

    def setposiçãox(self,posiçãoxmudou):
        self.posição_x=posiçãoxmudou
    def getForça(self):
        return self.força

    def getposiçãox(self):
        return self.posição_x

class Galinha (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)   
class Gato (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)
class Cachorro (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)
class Vaca (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)
class Leao (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)
class Raposo (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)
class Doraa (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)
class Botas (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y) 
class Estrelinha(Animal):
    def __init__ (self,nome,força,posição_x,posição_y,posição_x2,posição_y2,posição_x3,posição_y3,posição_x4,posição_y4):
        super(). __init__ (nome,força,posição_x,posição_y)
        self.posição_x2=int(posição_x2)
        self.posição_y2=int(posição_y2)
        self.posição_x3=int(posição_x3)
        self.posição_y3=int(posição_y3)
        self.posição_x4=int(posição_x4)
        self.posição_y4=int(posição_y4)
class PorcoEspinho(Animal):
    def __init__ (self,nome,força,posição_x,posição_y,posição_x2,posição_y2):
        super(). __init__ (nome,força,posição_x,posição_y)
        self.posição_x2=int(posição_x2)
        self.posição_y2=int(posição_y2)  
class Espinho(Animal):
     def __init__ (self,nome,força,posição_x,posição_y,posição_x2,posição_y2,posição_x3,posição_y3,posição_x4,posição_y4,posição_x5,posição_y5,posição_x6,posição_y6):
        super(). __init__ (força,posição_x,posição_y,posição_x2,posição_y2,posição_x3,posição_y3,posição_x4,posição_y4,posição_x5,posição_y5,posição_x6,posição_y6)
        self.posição_x2=int(posição_x2)
        self.posição_y2=int(posição_y2)
        self.posição_x3=int(posição_x3) 
        self.posição_y3=int(posição_y3)
        self.posição_x4=int(posição_x4) 
        self.posição_y4=int(posição_y4)
        self.posição_x5=int(posição_x5) 
        self.posição_y5=int(posição_y5)
        self.posição_x6=int(posição_x6) 
        self.posição_y6=int(posição_y6)
class Cow(Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)


#Caracteristicas
leao= Leao ('Leão Simba',50,250,125)
vaca= Vaca ('Vaca Maggie',30,80,235)
cachorro = Cachorro ('Dog Caramelo',15,313,18)
gato = Gato ('Gato Caua',10,140,340)
galinha = Galinha ('Galinha Margarete',5,370,230)
botas = Botas ('Botas',0,32,5)
raposo = Raposo ('Raposo',100,80,10)
dora = Doraa ('Dora',10,430,15)
estrela = Estrelinha ('Dalva',5,210,360,40,310,375,210,95,160)#a ultima(ex4) e a penultima (ex3) sao a da galinha e gato, 1 é a sozminah
porquinho= PorcoEspinho ('Porquinho José',5,32,80,410,340)
vaquinha = Cow ('Denny',0,32,80)

import pygame
pygame.init()
from random import randint

janela = pygame.display.set_mode((1000,500))
fundo_jogo = pygame.image.load('imagens_do_pygame/tela.tabuleiro.verde.png')
pygame.display.set_caption('Tabuleiro da Dora')
DEFAULT_IMAGE_SIZE = (1000, 500)
fundo = pygame.transform.scale(fundo_jogo, DEFAULT_IMAGE_SIZE)

#imagens 
doraimagem = pygame.image.load('imagens_do_pygame/dora.sem.fundo.png')
botasimagem = pygame.image.load('imagens_do_pygame/botas.sem.fundo.png')
leaoimagem = pygame.image.load('imagens_do_pygame/leao.direita.png')
vacaimagem = pygame.image.load('imagens_do_pygame/vaca.esquerda.png')
galinhaimagem = pygame.image.load('imagens_do_pygame/galinha.direita.png')
gatoimagem = pygame.image.load('imagens_do_pygame/gato1.png')
cachorroimagem = pygame.image.load('imagens_do_pygame/dog1.png')
raposoimagem = pygame.image.load('imagens_do_pygame/raposo1.png')
porquinhoimagem = pygame.image.load('imagens_do_pygame/porquinho1.png')
starimagem = pygame.image.load('imagens_do_pygame/estrelinha.png')
vaquinhaimagem = pygame.image.load('imagens_do_pygame/vaquinha.png')

#posicoes dos animais 
x=dora.posição_x
y=dora.posição_y
xbotas=botas.posição_x
ybotas=botas.posição_y
xleao= leao.posição_x
yleao= leao.posição_y
xvaca= vaca.posição_x
yvaca=vaca.posição_y
xgalinha=galinha.posição_x
ygalinha=galinha.posição_y
xgato=gato.posição_x
ygato=gato.posição_y
xdog=cachorro.posição_x
ydog=cachorro.posição_y
xraposo=raposo.posição_x
yraposo=raposo.posição_y
xvaquinha=vaquinha.posição_x
yvaquinha=vaquinha.posição_y
xestrelinha= estrela.posição_x
yestrelinha = estrela.posição_y
x2estrelinha= estrela.posição_x2
y2estrelinha = estrela.posição_y2
x3estrelinha= estrela.posição_x3
y3estrelinha = estrela.posição_y3
x4estrelinha= estrela.posição_x4
y4estrelinha = estrela.posição_y4

#posição porquinho
xporquinho= porquinho.posição_x
yporquinho= porquinho.posição_y
x2porquinho= porquinho.posição_x2
y2porquinho= porquinho.posição_y2

#fonte
fonte=pygame.font.SysFont('Helvetica',40,True,False)
fonte2=pygame.font.SysFont('Helvetica',20,True,False)

#textos de forças
mraposo = f'Força do {raposo.nome}:{raposo.força}'
textraposo = fonte2.render(mraposo, True,(255,255,255))

mgato = f'Força do {gato.nome}:{gato.força}'
textgato = fonte2.render(mgato, True,(255,255,255))

mvaca = f'Força da {vaca.nome}:{vaca.força}'
textvaca = fonte2.render(mvaca, True,(255,255,255))

mdog = f'Força do {cachorro.nome}:{cachorro.força}'
textdog = fonte2.render(mdog, True,(255,255,255))

mleao = f'Força do {leao.nome}:{leao.força}'
textleao = fonte2.render(mleao, True,(255,255,255))

mgalinha = f'Força da {galinha.nome}:{galinha.força}'
textgalinha = fonte2.render(mgalinha, True,(255,255,255))


pontos=dora.força

#teclas de movimento e janelas
janelaaberta=True
while janelaaberta:
    pygame.time.delay(50)
    mensagem = f'Força da Dora:{pontos}'
    texto_formatado= fonte.render(mensagem, True,(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janelaaberta=False
    comandos = pygame.key.get_pressed()
    velocidade_porquinho=9
    if comandos[pygame.K_UP]and y>=25: #cima
        y=y-51.50
    if comandos[pygame.K_DOWN]and y<=340: #baixo
        y=y+51.50
    if comandos[pygame.K_RIGHT]and x<=410: #direita
        x=x+56.25
    if comandos[pygame.K_LEFT]and x>=50:  #esquerda
        x=x-56.25

    #loop do porquinhos
    if xporquinho < 0 or xporquinho > 410:
        velocidade_porquinho = -velocidade_porquinho
        xporquinho = 50

    xporquinho += velocidade_porquinho
    #porquinho2
    if x2porquinho < 0 or x2porquinho >410:
        velocidade_porquinho = -velocidade_porquinho
        x2porquinho = 40

    x2porquinho += velocidade_porquinho
    

    #casos porquinho1
    if  (x-80 < xporquinho and y+80 > yporquinho and y-80 < yporquinho):
        doraimagem= pygame.image.load('imagens_do_pygame/dora4.png')
        if (x-40 < xporquinho and x+40> xporquinho and y+40 > yporquinho and y-40 < yporquinho):
            if dora.força >= porquinho.força:
                yporquinho=4000
                print('Dora Ganhou')
                dora.setforça(dora.força-porquinho.força)
                pontos=dora.força
                doraimagem = pygame.image.load('imagens_do_pygame/dora.sem.fundo.png')
            elif dora.força<=porquinho.força:
                dora.setforça(dora.força-dora.força)
                pontos=dora.força
                print('Dora Morreu!')
                yleao=4000
                ygalinha=4000
                yvaca=4000
                yraposo=4000
                ygato=4000
                ydog=4000
                yporquinho=4000
                y2porquinho=4000
                ybotas=4000
                yestrelinha=4000
                y2estrelinha=4000
                y3estrelinha=4000
                y4estrelinha=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
    #casos porquinho2
    if  (x-80 < x2porquinho and y+80 > y2porquinho and y-80 < y2porquinho):
        doraimagem= pygame.image.load('imagens_do_pygame/dora4.png')
        if (x-40 < x2porquinho and x+40> x2porquinho and y+40 > y2porquinho and y-40 < y2porquinho):
            if dora.força >= porquinho.força:
                y2porquinho=4000
                print('Dora Ganhou')
                dora.setforça(dora.força-porquinho.força)
                pontos=dora.força
                doraimagem = pygame.image.load('imagens_do_pygame/dora.sem.fundo.png')
            elif dora.força<=porquinho.força:
                dora.setforça(dora.força-dora.força)
                pontos=dora.força
                print('Dora Morreu!')
                yleao=4000
                ygalinha=4000
                yvaca=4000
                yraposo=4000
                ygato=4000
                ydog=4000
                yporquinho=4000
                y2porquinho=4000
                ybotas=4000
                yestrelinha=4000
                y2estrelinha=4000
                y3estrelinha=4000
                y4estrelinha=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                
                #casos raposo
    if (x-80 < xraposo and y+80 > yraposo and y-80 < yraposo):
        doraimagem= pygame.image.load('imagens_do_pygame/dora4.png')
        if (x-60 < xraposo and y+60 > yraposo and y-40 < yraposo):
            if dora.força >= raposo.força:
                yraposo=4000
                yporquinho=4000
                print('Dora Ganhou')
                doraimagem= pygame.image.load('imagens_do_pygame/dora5.png')
                dora.setforça(dora.força+raposo.força)
                raposo.setforça(raposo.força-raposo.força)
                pontos=dora.força

            elif dora.força<=raposo.força:
                dora.setforça(dora.força-dora.força)
                pontos=dora.força
                print('Dora Morreu!')
                yleao=4000
                ygalinha=4000
                yvaca=4000
                yraposo=4000
                ygato=4000
                ydog=4000
                yporquinho=4000
                y2porquinho=4000
                ybotas=4000
                yestrelinha=4000
                y2estrelinha=4000
                y3estrelinha=4000
                y4estrelinha=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                
    
            #casos leao
    if (x-80 < xleao and y+80 > yleao and y-80 < yleao and y-80 < yleao):
        doraimagem= pygame.image.load('imagens_do_pygame/dora4.png')
        if (x-40 < xleao and x+40> xleao and y+40 > yleao and y-40 < yleao):
            if dora.força >= leao.força:
                yleao=4000
                print('Dora Ganhou')
                dora.setforça(dora.força+leao.força)
                leao.setforça(leao.força-leao.força)
                pontos=dora.força
                doraimagem = pygame.image.load('imagens_do_pygame/dora.sem.fundo.png')
            elif dora.força<=leao.força:
                dora.setforça(dora.força-dora.força)
                pontos=dora.força
                print('Dora Morreu!')
                yleao=4000
                ygalinha=4000
                yvaca=4000
                yraposo=4000
                ygato=4000
                ydog=4000
                yporquinho=4000
                y2porquinho=4000
                yestrelinha=4000
                y2estrelinha=4000
                y3estrelinha=4000
                y4estrelinha=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                
                #casos galinha       
    if (x-80 < xgalinha and y+80 > ygalinha and y-80 < ygalinha and y-80 < ygalinha):
        doraimagem= pygame.image.load('imagens_do_pygame/dora4.png')
        if (x-40 < xgalinha and x+40> xgalinha and y+40 > ygalinha and y-40 < ygalinha):
            if dora.força >= galinha.força:
                ygalinha=4000
                print('Dora Ganhou')
                dora.setforça(dora.força+galinha.força)
                galinha.setforça(galinha.força-galinha.força)
                pontos=dora.força
                doraimagem = pygame.image.load('imagens_do_pygame/dora.sem.fundo.png')
            elif dora.força<=galinha.força:
                dora.setforça(dora.força-dora.força)
                pontos=dora.força
                print('Dora Morreu!')
                yleao=4000
                ygalinha=4000
                yvaca=4000
                yraposo=4000
                ygato=4000
                ydog=4000
                yporquinho=4000
                y2porquinho=4000
                ybotas=4000
                yestrelinha=4000
                y2estrelinha=4000
                y3estrelinha=4000
                y4estrelinha=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                
            
            #casos gato
    if (x-80 < xgato and y+80 > ygato and y-80 < ygato and y-80 < ygato):
        doraimagem= pygame.image.load('imagens_do_pygame/dora4.png')
        if (x-20 < xgato and x+20> xgato and y+20 > ygato and y-20 < ygato):
            if dora.força >= gato.força:
                ygato=4000
                print('Dora Ganhou')
                dora.setforça(dora.força+gato.força)
                gato.setforça(gato.força-gato.força)
                pontos=dora.força
                doraimagem = pygame.image.load('imagens_do_pygame/dora.sem.fundo.png')
            elif dora.força<=gato.força:
                dora.setforça(dora.força-dora.força)
                pontos=dora.força
                print('Dora Morreu!')
                yleao=4000
                ygalinha=4000
                yvaca=4000
                yraposo=4000
                ygato=4000
                ydog=4000
                yporquinho=4000
                y2porquinho=4000
                ybotas=4000
                yestrelinha=4000
                y2estrelinha=4000
                y3estrelinha=4000
                y4estrelinha=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png') 
                

            #casos vaca
    if (x-80 < xvaca and y+80 > yvaca and y-80 < yvaca and y-80 < yvaca):
        doraimagem= pygame.image.load('imagens_do_pygame/dora4.png')
        if (x-20 < xvaca and x+20> xvaca and y+20 > yvaca and y-20 < yvaca):
            if dora.força >= vaca.força:
                yvaca=4000
                print('Dora Ganhou')
                dora.setforça(dora.força+vaca.força)
                vaca.setforça(vaca.força-vaca.força)
                pontos=dora.força
                doraimagem = pygame.image.load('imagens_do_pygame/dora.sem.fundo.png')
            elif dora.força<=vaca.força:
                dora.setforça(dora.força-dora.força)
                pontos=dora.força
                print('Dora Morreu!')
                yleao=4000
                ygalinha=4000
                yvaca=4000
                yraposo=4000
                ygato=4000
                ydog=4000
                yporquinho=4000
                y2porquinho=4000
                ybotas=4000
                yestrelinha=4000
                y2estrelinha=4000
                y3estrelinha=4000
                y4estrelinha=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                
               

            #casos doguinho 
    if (x-80 < xdog and y+80 > ydog and y-80 < ydog and y-80 < ydog):
        doraimagem= pygame.image.load('imagens_do_pygame/dora4.png')
        if (x-20 < xdog and x+20> xdog and y+20 > ydog and y-20 < ydog):
            if dora.força >= cachorro.força:
                ydog=4000
                print('Dora Ganhou')
                dora.setforça(dora.força+cachorro.força)
                cachorro.setforça(cachorro.força-cachorro.força)
                pontos=dora.força
                doraimagem = pygame.image.load('imagens_do_pygame/dora.sem.fundo.png')
            elif dora.força<=cachorro.força:
                dora.setforça(dora.força-dora.força)
                pontos=dora.força
                print('Dora Morreu!')
                yleao=4000
                ygalinha=4000
                yvaca=4000
                yraposo=4000
                ygato=4000
                ydog=4000
                yporquinho=4000
                y2porquinho=4000
                ybotas=4000
                yestrelinha=4000
                y2estrelinha=4000
                y3estrelinha=4000
                y4estrelinha=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                      
    
                #ganhos de estrelas
    if (x-30 < xestrelinha and x+30> xestrelinha and y+30 > yestrelinha and y-30 < yestrelinha):
                yestrelinha=4000
                print('Dora Ganhou')                                    #certo
                dora.setforça(dora.força+estrela.força)
                estrela.setforça(estrela.força-estrela.força)
                estrela.setforça(estrela.força+5)
                pontos=dora.força 
    if (x-60 < x2estrelinha and x+60> x2estrelinha and y+60 > y2estrelinha and y-60 < y2estrelinha):
                y2estrelinha=4000
                print('Dora Ganhou')
                dora.setforça(dora.força+estrela.força)
                estrela.setforça(estrela.força-estrela.força)   
                estrela.setforça(estrela.força+5)
                pontos=dora.força          
    if (x-30 < x3estrelinha and x+30> x3estrelinha and y+30 > y3estrelinha and y-30 < y3estrelinha):
                y3estrelinha=4000
                print('Dora Ganhou')
                dora.setforça(dora.força+estrela.força)
                estrela.setforça(estrela.força-estrela.força)
                estrela.setforça(estrela.força+5)
                pontos=dora.força
    if (x-35 < x4estrelinha and x+35> x4estrelinha and y+35 > y4estrelinha and y-35 < y4estrelinha):
                y4estrelinha=4000
                print('Dora Ganhou')
                dora.setforça(dora.força+estrela.força)
                estrela.setforça(estrela.força-estrela.força)
                estrela.setforça(estrela.força+5)
                pontos=dora.força
    
    #textos
    janela.blit(fundo,(0,0))
    janela.blit(texto_formatado,(600,40))
    janela.blit(textraposo,(600,100))
    janela.blit(textgato,(600,140))
    janela.blit(textleao,(600,180))
    janela.blit(textvaca,(600,220))
    janela.blit(textdog,(600,260))
    janela.blit(textgalinha,(600,300))


    #imagens
    janela.blit(doraimagem,(x,y))
    janela.blit(botasimagem,(xbotas,ybotas))
    janela.blit(leaoimagem,(xleao,yleao))
    janela.blit(vacaimagem,(xvaca,yvaca))
    janela.blit(galinhaimagem,(xgalinha,ygalinha))
    janela.blit(gatoimagem,(xgato,ygato))
    janela.blit(cachorroimagem,(xdog,ydog))
    janela.blit(raposoimagem,(xraposo,yraposo))
    janela.blit(vaquinhaimagem,(xvaquinha,yvaquinha))

    janela.blit(starimagem,(xestrelinha,yestrelinha))
    janela.blit(starimagem,(x2estrelinha,y2estrelinha))
    janela.blit(starimagem,(x3estrelinha,y3estrelinha))
    janela.blit(starimagem,(x4estrelinha,y4estrelinha))
    
    janela.blit(porquinhoimagem,(xporquinho,yporquinho))
    janela.blit(porquinhoimagem,(x2porquinho,y2porquinho))

    pygame.display.update()

pygame.quit()

