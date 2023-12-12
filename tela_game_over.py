
from tkinter import *
import tkinter as tk

def retornar():
    import Telas

root_go=tk.Tk()
root_go.title('NÍVEIS DE JOGO')
root_go.geometry('1076x717')
root_go.resizable(True,True)

imagem_game_over = PhotoImage( file="imagens_do_tkinter/game over.png", master=root_go)
imagem__game_over = tk.Label(root_go, image=imagem_game_over).pack()


imagem_seta = PhotoImage(file='imagens_do_tkinter/seta.png',master=root_go)
imagem_seta = imagem_seta.subsample(1,1)
botao_seta = tk.Label(root_go, image=imagem_seta)
botao_seta.image = imagem_seta


botao_retornar = tk.Button (root_go,image=imagem_seta,command=retornar)
botao_retornar.place(x = 465, y = 400)


configuraçãoGO()
  