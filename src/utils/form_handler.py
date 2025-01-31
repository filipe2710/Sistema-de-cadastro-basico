
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import messagebox
   
class Form_handler:
   def __init__(self, name_entry, telefone_entry, codigo_entry, cidade_entry):
     self.name_entry = name_entry
     self.telefone_entry = telefone_entry
     self.codigo_entry = codigo_entry
     self.cidade_entry = cidade_entry
     
   def get_entry_value(self, entry):
     if entry is None:
       return None
     value = entry.get().strip()
     if value in  ["Digite o nome do cliente", "Digite o telefone do cliente", "Digite a cidade do cliente"]:
       return ""
     return value

   def save_data(self):  # função de salvar os dados
      self.name = self.get_entry_value(self.name_entry)
      self.telefone = self.get_entry_value(self.telefone_entry)
      self.codigo = self.get_entry_value(self.codigo_entry)
      self.cidade = self.get_entry_value(self.cidade_entry)

       # salvar dados na base de dados
   def db_save(name, telefone, codigo, city):
     # lógica para salvar dados na base de dados
     pass
   
     