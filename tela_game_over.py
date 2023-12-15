from tkinter import *
import tkinter as tk
root=Tk()

class configuração():
    def __init__(self, master=None):
        self.master = master
        self.root = root
        self.tela()
        root.mainloop() 

    def tela(self): #nome da janela
        self.root.title('DORA CARNICEIRA 0.2')
        self.root.geometry('0x0')
        self.root.resizable(True,True)

def retornar():
    import Telas

root_go=tk.Tk()
root_go.title('VC MORREU')
root_go.geometry('1076x717')
root_go.resizable(True,True)

imagem_game_over = PhotoImage( file="imagens_do_tkinter/game over.png", master=root_go)
imagem__game_over = tk.Label(root_go, image=imagem_game_over).pack()

#seta game over
imagem_seta = PhotoImage(file='imagens_do_tkinter/seta.png',master=root_go)
imagem_seta = imagem_seta.subsample(1,1)
botao_seta = tk.Label(root_go, image=imagem_seta)
botao_seta.image = imagem_seta
botao_retornar = tk.Button (root_go,image=imagem_seta,command=retornar)
botao_retornar.place(x = 465, y = 400)

root.withdraw()
root_go.mainloop() #DEVERIA MANDAR PARA P TELA INCIAL