
  
class Form_handler:
   def __init__(self):
     pass
   
   def save_data(self, name, telefone, codigo, city):
     # lógica para verificar valores dos campos e salvar
     name = self.name_entry.get_value()
     if name == "Digite o nome do cliente":
       name = ""
       
     telefone = self.telefone_entry.get_value()
     if telefone == "Digite o telefone do cliente":
       telefone = ""
       
     codigo = self.codigo_entry.get_value()
     if codigo == "":
       codigo = 0
       
     city = self.cidade_entry.get_value()
     if city == "Digite a cidade do cliente":
       city = ""
       
       
       # salvar dados na base de dados
   def db_save(name, telefone, codigo, city):
     # lógica para salvar dados na base de dados
     pass
   
     