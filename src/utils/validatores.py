
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.Format_entry import format_entry

class validators(format_entry):
#    def __init__(self, root):
#        self.root = root
#        self.vcmd_telefone = root.register(self.telefone_validate)
#        self.vcmd_codigo = (root.register(self.codigo_validate), "%d", "%P", "%s")
#        self.vcmd_name = (root.register(self.name_validate), "%d", "%P", "%s")
#        self.vcmd_city = (root.register(self.city_validate), "%d", "%P", "%s")
#        self.vcmd_zip_code = (root.register(self.zip_code_validate), "%d", "%P", "%s")
#        self.vcmd_address = (root.register(self.address_validate), "%d", "%P", "%s")  # Validador de endereço
        
    
    def phone_validate(self, action, value_if_allowed, text):        
        """
        Valida a entrada para o campo de telefone.
        Permite apenas números e caracteres específicos (ex.: '(', ')', '-', ' ').
        """

        if action == '1':  # Inserção de caractere
            # Remove qualquer formatação temporariamente para validar os números
            clean_value = value_if_allowed.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
            
            # Permite apenas números
            if not clean_value.isdigit():
                return False
            
            # Limita o comprimento total (apenas números) a 11 caracteres (DDD + número)
            if len(clean_value) > 11:
                return False
            
            # Aplica formatação automática
            formatted_value = clean_value
            if len(clean_value) >= 1:
                formatted_value = f"({clean_value[:2]}"
            if len(clean_value) >= 3:
                formatted_value += f") {clean_value[2:6]}"
            if len(clean_value) > 6:
                formatted_value = f"{formatted_value[:9]}-{clean_value[6:]}"
            
            # Atualiza o campo de texto com o valor formatado
            self.root.after(1, lambda: self.root.focus_get().delete(0, "end"))
            self.root.after(1, lambda: self.root.focus_get().insert(0, formatted_value))
            
            return True
        elif action == '0':  # Remoção de caractere
            return True
        
        return False
    
    
    def codigo_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            if value_if_allowed.isdigit():
                return True
        return False
             
    def name_validate (self, action, value_if_allowed, text):    
        if action == '1':  # insert
            if value_if_allowed == "Digite o nome do cliente":
                return True
            if not value_if_allowed.strip():
                return True
            if not value_if_allowed.isalpha() and not value_if_allowed.isspace():
                return False
        
            
    def city_validate(self, action, value_if_allowed, text):
        if action == '1': # insert
            if value_if_allowed == "Digite a cidade do cliente":
                return True
            if not value_if_allowed.isalpha() and not value_if_allowed.isspace():
                return False
        
    def zip_code_validate(self, action, value_if_allowed, text):
        if action == '1':  # Inserção de caractere
            if len(value_if_allowed) > 9:
                return False
            if all(char.isdigit() for char in value_if_allowed.replace('-', '')):
                self.format_zip_code(value_if_allowed)
                return True
        elif action == '0':  # Remoção de caractere
            return True
        return False

    
    def address_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.-/"
            if value_if_allowed == "Digite o endereço do cliente":
                return True
            if all(char in allowed_chars for char in value_if_allowed): # verifica se todos os  caracteres são permitidos
                return True
            else:
                return False
            
    
# test
    
    