import tkinter as tk
from tkinter import PhotoImage

def abrir_nova_janela():
    root.withdraw()  # Oculta a janela atual
    root2.deiconify()  # Exibe a nova janela
def voltar_para_primeira_janela():
    root2.withdraw()  # Oculta a nova janela
    root.deiconify()  # Exibe a primeira janela
def abrir_NIVEL01():
    root2.withdraw()
    import nivel01
def abrir_NIVEL02():
    root2.withdraw()
    import nivel02
def abrir_NIVEL03():
    root2.withdraw()
    import nivel03

# Criar a primeira janela
root = tk.Tk()
root.title('DORA CARNICEIRA 0.2')
root.geometry('1076x717')
root.resizable(True,True)

# imagem da primeira janela
imagem_menu = PhotoImage( file="imagens_do_tkinter/Dora carniceiraa.png", master=root) 
imagem__menu = tk.Label(root, image=imagem_menu).pack()

#botao da primeira janela (start)
imagem_start = PhotoImage(file='imagens_do_tkinter/start.png')
imagem_start = imagem_start.subsample(1,1)
botao_start = tk.Label(root, image=imagem_start) 
botao_start.image = imagem_start
botao_menu = tk.Button (root,image=imagem_start, command=abrir_nova_janela)
botao_menu.place(x = 200, y = 500)


# Criar a segunda janela 
root2 = tk.Toplevel(root)
root2.title('NÍVEIS DE JOGO')
root2.geometry('1076x717')
root2.resizable(True,True)

#imagem da segunda janela
imagem_niveis = PhotoImage( file="imagens_do_tkinter/niveis.png")
imagem__niveis = tk.Label(root2, image=imagem_niveis).pack()
  
#botao para voltar pro menu (segunda janela)
imagem_voltar = PhotoImage(file='imagens_do_tkinter/botao menu.png') #imagem do botao 'menu'
botao_voltar = tk.Label(root2, image=imagem_voltar) #qnd aperta no botao 'menu' vai p algum lugar
botao_voltar.image = imagem_voltar 
#
botao_voltar_menu=tk.Button(root2, image=imagem_voltar, command=voltar_para_primeira_janela)
botao_voltar_menu.place(x = 900, y = 550)

#BOTAO NIVEL01 (segunda janela)
imagem_start1 = PhotoImage(file='imagens_do_tkinter/start.png')
imagem_start1 = imagem_start1.subsample(1,1)
botao_start1 = tk.Label(root2, image=imagem_start1)
botao_start1.image = imagem_start1
botao_nivel1 = tk.Button (root2,image=imagem_start1, command = abrir_NIVEL01)
botao_nivel1.place(x = 100, y = 380)

#BOTÃO NIVEL02 (segunda janela)
imagem_start2 = PhotoImage(file='imagens_do_tkinter/start.png')
imagem_start2 = imagem_start1.subsample(1,1)
botao_start2 = tk.Label(root2, image=imagem_start2)
botao_start2.image = imagem_start1
botao_nivel2 = tk.Button (root2,image=imagem_start1, command = abrir_NIVEL02)
botao_nivel2.place(x = 260, y = 380)

#BOTÃO NIVEL03
imagem_start3 = PhotoImage(file='imagens_do_tkinter/start.png')
imagem_start3 = imagem_start1.subsample(1,1)
botao_start3 = tk.Label(root2, image=imagem_start3)
botao_start3.image = imagem_start1
botao_nivel3 = tk.Button (root2,image=imagem_start1, command = abrir_NIVEL03)
botao_nivel3.place(x = 420, y = 380)

#criando a tela game over
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

# Ocultar a nova janela inicialmente
root2.withdraw()
# Iniciar o loop principal
root.mainloop()