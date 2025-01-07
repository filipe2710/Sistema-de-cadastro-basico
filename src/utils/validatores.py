

class validators():
    def __init__(self, root):
        self.root = root
        self.vcmd_telefone = root.register(self.telefone_validate)
        self.vcmd_codigo = root.register(self.codigo_validate)
        self.vcmd_name = root.register(self.name_validate)
        self.vcmd_city = root.register(self.city_validate)
        self.vcmd_zip_code = root.register(self.zip_code_validate)
                
    def telefone_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            if not value_if_allowed.strip():
                return True
            if not value_if_allowed.replace("(", "").replace(")", "").replace("-", "").isdigit():
                return False
            if len(value_if_allowed) > 15:
                return False
        return True
    
    def codigo_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
             if value_if_allowed.isdigit():
                 return True
             return False
        return True
             
    def name_validate (self, action, value_if_allowed, text):    
        if value_if_allowed == "Digite o nome do cliente":
            return True
        if action == '1':  # insert
            if not value_if_allowed.strip():
                return True
            if not value_if_allowed.isalpha() and not value_if_allowed.isspace():
                return False
        return True
            
    def city_validate(self, action, value_if_allowed, text):
        if action == '1': # insert
            if value_if_allowed == "Digite a cidade do cliente":
                return True
            if not value_if_allowed.isalpha() and not value_if_allowed.isspace():
                return False
        return True
    
    def zip_code_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            if value_if_allowed == "Digite o CEP do cliente":
                return True
            if not value_if_allowed.strip():
                return True
            if value_if_allowed.isdigit() and len(value_if_allowed) == 8:
                return True
        return False
    
    
# test
    
        