

class validators():
    def __init__(self, root):
        self.root = root
        #self.vcmd_telefone = root.register(self.telefone_validate)
        self.vcmd_codigo = root.register(self.codigo_validate)
        self.vcmd_name = root.register(self.name_validate)
        self.vcmd_city = root.register(self.city_validate)
        self.vcmd_zip_code = root.register(self.zip_code_validate)
                
    
    def telefone_validate(self, action, value_if_allowed, text):        
        """
        Valida a entrada para o campo de telefone.
        Permite apenas números e caracteres específicos (ex.: '(', ')', '-', ' ').
        """

        if action == '1':  # Inserção de um caractere
            if value_if_allowed == "Digite o telefone do cliente":  
                return True
            # Permite apenas números e caracteres válidos de formatação de telefone
            if all(c.isdigit() or c in "()- " for c in value_if_allowed):
                # Limita o comprimento do telefone a 15 caracteres
                if len(value_if_allowed) <= 15:
                    return True
            else:
                return False

    def codigo_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            if value_if_allowed == "Id":
                return True
            if value_if_allowed.isdigit():
                return True
            else:
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
        if action == '1':  # insert
            if value_if_allowed == "Digite o CEP do cliente":
                return True
            if len(value_if_allowed) <= 13 and value_if_allowed.isdigit():
                return True
            else:
                return False
    
    
# test
    
        