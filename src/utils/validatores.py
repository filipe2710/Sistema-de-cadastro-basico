

class validators():
    def __init__(self, root):
        self.root = root
        self.vcmd_telefone = (root.register(self.telefone_validate), "%d", "%P", "%s")
        self.vcmd_codigo = (root.register(self.codigo_validate), "%d", "%P", "%s")
        self.vcmd_name = (root.register(self.name_validate), "%d", "%P", "%s")
        self.vcmd_city = (root.register(self.city_validate), "%d", "%P", "%s")
        
        
    def telefone_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            if value_if_allowed == "Digite o telefone do cliente":
                return False
            if not value_if_allowed.strip():
                return True
            if not value_if_allowed.replace("(", "").replace(")", "").replace("-", "").isdigit():
                return False
            if len(value_if_allowed) > 15:
                return False
        return True
    
    def codigo_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            if not value_if_allowed.strip():
                return True
            if value_if_allowed.isdigit():
                return True
        return False
            
            
    def name_validate (self, action, value_if_allowed, text):
        if action == '1':  # insert
            if not value_if_allowed.strip():
                return True
            if not value_if_allowed.isalpha() and not value_if_allowed.isspace:
                return False
        return True
            
    def city_validate(self, action, value_if_allowed, text):
        if action == '1': # insert
            if value_if_allowed == "Digite a cidade do cliente":
                return False
            if not value_if_allowed.isalpha() and not value_if_allowed.isspace:
                return False
        return True
    
    
# test
    
        