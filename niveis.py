from tkinter import *
import tkinter as tk

root2=Tk()

class configuração2():
    def __init__(self, master=None):
        self.master = master
        self.root2 = root2
        self.tela2()
        root2.mainloop()

    def tela2(self):
        self.root2.title('NÍVEIS DE JOGO')
        self.root2.geometry('1076x717')
        self.root2.resizable(True,True)

imagem_niveis = PhotoImage( file="imagens_do_tkinter/niveis.png", master=root2)
imagem__niveis = Label(root2, image=imagem_niveis).pack()
    
configuração2()