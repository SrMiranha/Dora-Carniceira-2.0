from tkinter import *
import tkinter as tk


def game_over():
    import tela_game_over

    

class Animal:#superclasse
    def __init__ (self,nome,força,posição_x,posição_y):#atributos
        self.nome=str(nome)  #O nome em maiusculo é o nome da variavel (atributo)
        self.força=int(força)
        self.posição_x=int(posição_x)
        self.posição_y=int(posição_y)

    def setNome(self,nomemudou):
        self.nome=nomemudou

    def setforça(self,forçamudou):
        self.força=forçamudou

    def setPosição_x(self,posição_xmudou):
        self.posição_x=posição_xmudou

    def setPosição_y(self,posição_ymudou):
        self.posição_y=posição_ymudou
    
    def getNome(self):
        return self.nome

    def getForça(self):
        return self.força

    def getPosição_x(self):
        return self.posição_x

    def getPosição_y(self):
        return self.posição_y

class Galinha (Animal):#subclasse
    def __init__ (self,nome,força,posição_x,posição_y,raça):
        super(). __init__ (nome,força,posição_x,posição_y) 
        self.raça=str(raça)
    def guinchar (self):#metodo
        print(f'O',self.Nome,'está guinchando!')
    def getRaça(self):
        return self.raça
    def setRaça(self,Raçamudou):
        self.raça=Raçamudou  
class Gato (Animal):#subclasse
    def __init__ (self,nome,força,posição_x,posição_y,raça):
        super(). __init__ (nome,força,posição_x,posição_y)
        self.raça= str(raça)
    def miar (self):#metodo
        print(f'O',self.Nome,'está miando!')
    def getRaça(self):
        return self.raça
    def setRaça(self,Raçamudou):
        self.raça=Raçamudou  
class Cachorro (Animal):#subclasse
    def __init__ (self,nome,força,posição_x,posição_y,raça):
        super(). __init__ (nome,força,posição_x,posição_y)
        self.raça= str(raça)
    def latir (self):#metodo
        print(f'O',self.Nome,'está latindo!')
    def getRaça(self):
        return self.raça
    def setRaça(self,Raçamudou):
        self.raça=Raçamudou
class Vaca (Animal):#subclasse
    def __init__ (self,nome,força,posição_x,posição_y,raça):
        super(). __init__ (nome,força,posição_x,posição_y)
        self.raça= str(raça)
    def mugir (self):#metodos
        print(f'A',self.Nome,'está mugindo!')
    def getRaça(self):
        return self.raça
    def setRaça(self,Raçamudou):
        self.raça=Raçamudou    
class Leao (Animal):#subclasse
    def __init__ (self,nome,força,posição_x,posição_y,raça):
        super(). __init__ (nome,força,posição_x,posição_y)
        self.raça= str(raça)
    def rugir (self): #metodos
        print(f'O',self.nome,'está rugindo!')
    def getRaça(self):
         return self.raça
    def setRaça(self,Raçamudou):
        self.raça=Raçamudou   
class Raposo (Animal):#subclasse
    def __init__ (self,nome,força,posição_x,posição_y,raça):
        super(). __init__ (nome,força,posição_x,posição_y)
        self.raça= str(raça)
    def uiva (self):#metodo
        print(f'A',self.nome,'está uivando!')
    def getRaça(self):
        return self.raça
    def setRaça(self,Raçamudou):
        self.raça=Raçamudou
class Doraa (Animal):
    def __init__ (self,nome,força,posição_x,posição_y):
        super(). __init__ (nome,força,posição_x,posição_y)
class Botas (Animal):
    def __init__ (self,nome,força,posição_x,posição_y,raça):
        super(). __init__ (nome,força,posição_x,posição_y) 
        self.raça= str(raça)
    def getRaça(self):
            return self.raça

    def setRaça(self,Raçamudou):
            self.raça=Raçamudou 
class PorcoEspinho(Animal):
    def __init__ (self,nome,força,posição_x,posição_y,posição_x2,posição_y2,raça):
        super(). __init__ (nome,força,posição_x,posição_y)
        self.posição_x2=int(posição_x2)
        self.posição_y2=int(posição_y2)
        self.raça= str(raça)
        def setPosição_x(self,posição_xmudou):
            self.posição_x2 = posição_x2mudou

        def setPosição_y(self,posição_ymudou):
            self.posição_y2=posição_y2mudou
        
        def getPosição_2x(self):
            return self.posição_x2

        def getPosição_2y(self):
            return self.posição_y2

        def getRaça(self):
            return self.raça

        def setRaça(self,Raçamudou):
            self.raça=Raçamudou





#Caracteristicas
leao= Leao ('Leão Simba',50,250,125,'Leão Africano')
vaca= Vaca ('Vaca Maggie',30,80,235,'Vaca Nelore')
cachorro = Cachorro ('Dog Caramelo',15,313,18,'Dog Vira-lata')
gato = Gato ('Gato Caua',10,140,340,'Gato Siâmes')
galinha = Galinha ('Galinha Margarete',5,370,230,'Galinha Caipira')
botas = Botas ('Botas',0,32,5,'Macaco Botas')
raposo = Raposo ('Raposo',100,80,10,'Raposo')
dora = Doraa ('Dora',10,430,15)
porquinho= PorcoEspinho ('Porquinho José',2,50,25,410,340,'Porco espinho')


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
xporquinho= randint (porquinho.posição_x,porquinho.posição_x2)
yporquinho = randint (porquinho.posição_y, porquinho.posição_y2)



fonte=pygame.font.SysFont('Helvetica',40,True,False)
fonte2=pygame.font.SysFont('Helvetica',20,True,False)



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


janelaaberta=True
while janelaaberta:
    pygame.time.delay(50)
    mensagem = f'Força da Dora:{pontos}'
    texto_formatado= fonte.render(mensagem, True,(255,255,255))
#teclas de movimento e janelas
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janelaaberta=False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]and y>=25: #cima
         y=y-51.50
    if comandos[pygame.K_DOWN]and y<=340: #baixo
        y=y+51.50
    if comandos[pygame.K_RIGHT]and x<=410: #direita
        x=x+56.25
    if comandos[pygame.K_LEFT]and x>=50:  #esquerda
        x=x-56.25
    


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
                ybotas=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                game_over()
        

                
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
                ybotas=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                game_over()
                

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
                ybotas=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                game_over()
                

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
                ybotas=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png') 
                game_over()

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
                ybotas=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                game_over()
               

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
                ybotas=4000
                doraimagem=pygame.image.load('imagens_do_pygame/dora6.png')
                game_over()
                
                




    
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
    janela.blit(porquinhoimagem,(xporquinho,yporquinho))
    pygame.display.update()

pygame.quit()

