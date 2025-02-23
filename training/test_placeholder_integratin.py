import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from modules import Tk, messagebox, sqlite3, Button
from utils.placeholder import entryplaceholder

def save_data():
  name = name_entry.get_value()
  phone = phone_entry.get_value()
  city = city_entry.get_value()
  
  if not name:
    messagebox.showerror('Error', 'Nome é obrigatório')
    return
  
  print(f"Salvando dados: Nome={name}, phone={phone}, city={city}")
  # Simulação de salvamento em banco de dados
  try:
      con = sqlite3.connect("test.db")
      cursor = con.cursor()
      cursor.execute(
          """CREATE TABLE IF NOT EXISTS clientes (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              phone TEXT,
              city TEXT
          )"""
      )
      cursor.execute(
          "INSERT INTO clientes (nome, phone, city) VALUES (?, ?, ?)",
          (name, phone, city),
      )
      con.commit()
      print("Dados salvos com sucesso no banco de dados!")
  except Exception as e:
      print(f"Erro ao salvar no banco: {e}")
  finally:
      con.close()


# Criação de janela
root = Tk()
root.geometry("400x300")

name_entry = entryplaceholder(root, placeholder="Digite o nome", color="gray")
name_entry.pack(pady=10)

phone_entry = entryplaceholder(root, placeholder="Digite o phone", color="gray")
phone_entry.pack(pady=10)

city_entry = entryplaceholder(root, placeholder="Digite a city", color="gray")
city_entry.pack(pady=10)

save_button = Button(root, text="Salvar", command=save_data)
save_button.pack(pady=20)

root.mainloop()