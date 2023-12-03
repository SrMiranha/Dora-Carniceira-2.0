from tkinter import *
import tkinter as tk

root=Tk()

class configuração():
    def __init__(self, master=None):
        self.master = master
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title('DORA CARNICEIRA 0.2')
        self.root.geometry('1076x717')
        self.root.resizable(True,True)

def janela02():
    import niveis







# def Janela_niveis():
#     root2= tk.Toplevel()
#     root2.title("NÍVEIS DE JOGO")
#     root2.geometry('1076x717')
#     root2.resizable(True,True)
#     imagem_niveis = tk.PhotoImage( file="imagens_do_tkinter/niveis.png", master=root2)
#     imagem__niveis = tk.Label(root2, image=imagem_niveis).pack()
    
#     root2.mainloop
        
    

#imagem do menu
imagem_menu = PhotoImage( file="imagens_do_tkinter/Dora carniceiraa.png", master=root)
imagem__menu = Label(root, image=imagem_menu).pack()

#botao do menu (start)
imagem_start = PhotoImage(file='imagens_do_tkinter/botao menu.png')
imagem_start = imagem_start.subsample(1,1)
botao_start = Label(root, image=imagem_start)
botao_start.image = imagem_start

botao = Button (root,image=imagem_start, command = janela02)
botao.place(x = 200, y = 500)

configuração()
