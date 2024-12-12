from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text="començando")
label.grid()

def ao_aperta_enter(event): 
    label.configure(text="voce apertou o enter")

def enter(event):
  label.configure(text="voce entrou no campo")
    
def leave(event):
    label.configure(text="voce saiu do campo")
    
def click(event):
  label.configure(text="voce clicou no campo")
    
def ondoubleclick(event):
  label.configure(text="voce double clicou no campo")
    
def b3_motion(event):
  label.configure(text="arasta o mouse para %d, %d" % (e.x, e.y ))
    

root.bind("<Enter>", enter)
root.bind("<Leave>", leave)
root.bind("<Return>", ao_aperta_enter)
root.bind("<1>", click)
root.bind("<Double-1>", ondoubleclick)
root.bind("<B3-Motion>", b3_motion)


root.mainloop()



'''
from tkinter import *
from tkinter import ttk

# Cria a janela principal
root = Tk()

# Cria e posiciona um rótulo na janela
label = ttk.Label(root, text="começando")
label.grid()

# Define uma função que será chamada quando a tecla Enter for pressionada
def ao_apertar_enter(event):
    label.configure(text="Você apertou o Enter")

# Associa o evento da tecla Enter à função
root.bind("<Return>", ao_apertar_enter)

# Inicia o loop principal da interface gráfica
root.mainloop()

'''