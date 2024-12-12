from tkinter import *
from tkinter import ttk
import time


root = Tk()
root.title("testing loading bar")
root.geometry("400x500")

def step_func():
  #progress1['value'] += 10
  #progress1.start(10)
  global running
  running = True
  progress1['value'] = 0
  update_progress()
  
  
def update_progress():
  global running
  if running and progress1['value'] < 100:
    progress1['value'] += 5
    root.after(2000, update_progress)
  elif progress1['value'] >= 100:
    running = False
  
  
def stop_func():
  global running
  running = False


progress1 = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress1.pack(pady=30)

button1 = Button(root, text="pogresso", command=step_func)
button1.pack(pady=40)

button2 = Button(root, text="Stop", command=stop_func)
button2.pack(pady=50)



root.mainloop()
