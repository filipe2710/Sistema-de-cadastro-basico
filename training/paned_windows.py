from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Paned windows")
root.geometry("400x600")

panel1 = PanedWindow(bd=4, relief="raised", bg="red")
panel1.pack(fill=BOTH, expand=1)

left_label = Label(panel1, text="Panel Esquerdo")
panel1.add(left_label)

panel2 = PanedWindow(panel1, orient=VERTICAL, bd=4, relief="raised", bg="red")
panel1.add(panel2)

top_label = Label(panel2, text="Panel em Cima") 
panel2.add(top_label)

bottom_label = Label(panel2, text="Panel em Baixo")
panel2.add(bottom_label)



root.mainloop()