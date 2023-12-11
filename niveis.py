from tkinter import *
import tkinter as tk
import sys
import os


root2=Tk()

def nivel1():
    import nivel01
    root2.destroy()
    

def retornar_niveis():
    niveis= sys.executable
    os.execl(niveis,niveis, * sys.argv)

class configuração2():
    def __init__(self, master=None):
        self.master = master
        self.root2 = root2
        self.tela2()
        root2.mainloop
    def tela2(self):
        self.root2.title('NÍVEIS DE JOGO')
        self.root2.geometry('1076x717')
        self.root2.resizable(True,True)


imagem_niveis = PhotoImage( file="imagens_do_tkinter/niveis.png", master=root2)
imagem__niveis = Label(root2, image=imagem_niveis).pack()
  
#botao nivel 1

imagem_start1 = PhotoImage(file='imagens_do_tkinter/start.png',master=root2)
imagem_start1 = imagem_start1.subsample(1,1)
botao_start1 = Label(root2, image=imagem_start1)
botao_start1.image = imagem_start1

botao_nivel1 = Button (root2,image=imagem_start1, command = nivel1)
botao_nivel1.place(x = 100, y = 380)



configuração2()