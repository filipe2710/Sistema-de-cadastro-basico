from tkinter import *
from tkinter import messagebox


root = Tk()

def Display():
  messagebox.showinfo("info", "só para voce saber")
  messagebox.showwarning("perigo", "atenção")
  messagebox.showerror("error", "ocorreu um error")
  
  nocancel = messagebox.askokcancel("o que voce acha? ", "devemos ir em frente?")
  print(nocancel)
  
  yescancel = messagebox.askyesno("o que voce acha? ", "por favor decide")
  print(yescancel)
  
  retrycancel = messagebox.askretrycancel("o que voce acha? ", "qual é a sua resposta?")
  print(retrycancel)
  
  answer = messagebox.askquestion("o que voce acha? ", "qual é a sua resposta")

b1 = Button(root, text="testando usuario", command=Display)
b1.pack()

root.mainloop()