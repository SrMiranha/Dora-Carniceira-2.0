from tkinter import *
import requests
class joguin: 
    def __init__(self,master=None):
       pass


root=Tk()
root.title('Dora carniceira')
root.geometry('1076x717')

#botoes
botao_menu_imagem = PhotoImage (file='botao menu.png', master=root)
botao_menu_imagem = botao_menu_imagem.subsample(2,2)

imagem_botao=Label(root, image=botao_menu_imagem)
imagem_botao.image= botao_menu_imagem



botao=Button(root,image= botao_menu_imagem)
botao.grid(column=0,row=1,padx=(60,0))


# #imagem menu
imagem_menu = PhotoImage( file="Dora carniceiraa.png")
imagem__menu = Label(root, image=imagem_menu)
imagem__menu.imagem_menu = imagem_menu
imagem__menu.pack()




#configuração de tela


root.resizable(True,True)
joguin(root)
root.mainloop()



















# import requests
# from tkinter import *

# root = Tk() #abrir janela

# root.title('Experimento')
# root.geometry('400x400')


# informaçoes_janela= Label(root, text = 'To aprendendo')
# informaçoes_janela.grid(column=0,row=0,padx=10,pady=10)


# botao_menu_imagem = PhotoImage (file='botao menu.png', master=root)
# botao_menu_imagem = botao_menu_imagem.subsample(2,2)

# imagem_botao=Label(root, image=botao_menu_imagem)
# imagem_botao.image= botao_menu_imagem

# botao=Button(root,image= botao_menu_imagem)
# botao.grid(column=0,row=1,padx=(60,0))

# text_exibir= Label(root, text='')
# text_exibir.grid(column=0,row=2,padx=10,pady=10)

# root.mainloop() #para fechar a janela (fica no final do codigo)
