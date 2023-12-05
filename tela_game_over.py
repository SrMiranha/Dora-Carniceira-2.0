
from tkinter import *
import tkinter as tk
import sys
import os

root_go=Tk()

class configuraçãoGO():
    def __init__(self, master=None):
        self.master = master
        self.root_go = root_go
        self.tela_go()
        
    def tela_go(self):
        self.root_go.title('NÍVEIS DE JOGO')
        self.root_go.geometry('1076x717')
        self.root_go.resizable(True,True)

def retornar_niveis():
    root_go.withdraw()
    niveis= sys.executable
    os.execl(niveis,niveis, * sys.argv)

imagem_game_over = PhotoImage( file="imagens_do_tkinter/game over.png", master=root_go)
imagem__game_over = Label(root_go, image=imagem_game_over).pack()


imagem_seta = PhotoImage(file='imagens_do_tkinter/seta.png',master=root_go)
imagem_seta = imagem_seta.subsample(1,1)
botao_seta = Label(root_go, image=imagem_seta)
botao_seta.image = imagem_seta


botao_retornar = Button (root_go,image=imagem_seta, command=lambda:retornar_niveis())
botao_retornar.place(x = 465, y = 400)


configuraçãoGO()
  