from tkinter import *
import tkinter as tk
import subprocess

class game:
    def __init__(self, master=None):
      self.master = master 
      self.master.title('Dora carniceira')
      self.imagem = tk.PhotoImage(file="imagens_do_tkinter/Dora carniceira.png")
      self.label = tk.Label(self.master, image=self.imagem)
      self.label.imagem = self.imagem
      self.label.place(x = 800,  y = 600)
      
      
      botton = tk.PhotoImage(file='imagens_do_tkinter/start_botton.png')
      label = tk.Label( image=botton)
      label.imagem = self.botton
      btn = Button(self.master, image = self.botton, command = abrir_pygame)
      btn.place(x = 150, y = 500)

      def abrir_pygame():
         subprocess.run(['python', 'InterfaceDora.py'])
         
 




root = tk.Tk()
game(root)
root.mainloop()
