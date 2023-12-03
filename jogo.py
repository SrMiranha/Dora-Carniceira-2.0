from tkinter import *
import tkinter as tk
class joguin: 
    def __init__(self,master=None):
       pass
root=tk.Tk()
imagem = tk.PhotoImage(file="Dora carniceiraa.png")
w = tk.Label(root, image=imagem)
w.imagem = imagem
w.pack()
root.title('Dora carniceira')
root.geometry('1076x717')
root.resizable(True,True)
joguin(root)
root.mainloop()

