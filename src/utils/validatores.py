
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.Format_entry import format_entry

class validators(format_entry):
    def phone_validate(self, action, value_if_allowed, text):        
        if action == '1':
            claan_value = value_if_allowed.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
            if not claan_value.isdigit():
                return False
            if len(claan_value) > 11:   
                return False
            return True
        elif action == '0':
            return True
        return False
        

    
    def codigo_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            if value_if_allowed.isdigit():
                return True
        return False
             
    def name_validate (self, action, value_if_allowed, text):    
        print(f"action={action}, value_if_allowed={value_if_allowed}, text={text}")  # Debug
        
        if action == '1':  # insert
            if value_if_allowed == "Digite o nome do cliente":
                return True
            if not value_if_allowed.strip():
                return False
            if all(c.isalpha() or c.isspace() for c in value_if_allowed):
                return True
            return False
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
            if not value_if_allowed.strip():
                return False
            if all(c.isalpha() or c.isspace() for c in value_if_allowed):
                return True
            return False
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
        return True
    
# test
    
    