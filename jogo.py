from tkinter import *
import tkinter as tk
import sys
import os

root=Tk()

class configuração():
    def __init__(self, master=None):
        self.master = master
        self.root = root
        self.tela()
        root.mainloop() 

    def tela(self): #nome da janela
        self.root.title('DORA CARNICEIRA 0.2')
        self.root.geometry('1076x717')
        self.root.resizable(True,True)

def janela02():
    import niveis
    root.withdraw()
    #iamgem do botao voltar
    imagem_voltar = PhotoImage(file='imagens_do_tkinter/botao menu.png', master=niveis.root2)
    imagem_voltar= imagem_voltar.subsample(1,1)
    botao_voltar = Label(niveis.root2, image=imagem_voltar)
    botao_voltar.image = imagem_voltar

    #Botao para voltar pro menu
    botao_voltar_menu=Button(niveis.root2, image=imagem_voltar, command= lambda:voltar_pro_menu())
    botao_voltar_menu.place(x = 900, y = 550)
    
    # função que retorna pro menu
    def voltar_pro_menu():
        niveis.root2.destroy()
        jogo= sys.executable
        os.execl(jogo,jogo, * sys.argv)

#imagem do menu
imagem_menu = PhotoImage( file="imagens_do_tkinter/Dora carniceiraa.png", master=root) 
imagem__menu = Label(root, image=imagem_menu).pack() # a dora grandona por toda tela

#botao do menu (start)
imagem_start = PhotoImage(file='imagens_do_tkinter/start.png')
imagem_start = imagem_start.subsample(1,1) # o tamanho da imagem
botao_start = Label(root, image=imagem_start) 
botao_start.image = imagem_start #transformou a imagem em botao

botao_menu = Button (root,image=imagem_start, command = janela02)
botao_menu.place(x = 200, y = 500) # coordenadas de onde o botao ta


configuração()
