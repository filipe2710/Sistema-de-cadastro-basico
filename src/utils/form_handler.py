
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
   

   def save_data(self):  # função de salvar os dados
      name = self.name_entry.get()
      telefone = self.telefone_entry.get()
      codigo = self.codigo_entry.get()
      city = self.cidade_entry.get()

    # Verifique e substitua o placeholder por vazio
      if name == "Digite o nome do cliente" or not name.strip():
          name = ""  # Substituir por string vazia
      if telefone == "Digite o telefone do cliente" or not telefone.strip():
          telefone = ""  # Substituir por string vazia
      if city == "Digite a cidade do cliente" or not city.strip():
          city = ""  # Substituir por string vazia
      if not codigo.strip():
          codigo = ""  # Substituir por string vazia ou 0, dependendo do seu caso
      
      # Atribui valores validados para os campos
      self.nome = name
      self.telefone = telefone
      self.codigo = codigo
      self.cidade = city

       # salvar dados na base de dados
   def db_save(name, telefone, codigo, city):
     # lógica para salvar dados na base de dados
     pass
   
     