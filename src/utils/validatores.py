

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
                return True
            if text in "0123456789":
                return True
            else:
                return False
    
    
    def codigo_validate(self, action, value_if_allowed, text):
        if action == '1':  # insert
            if value_if_allowed.isdigit():
                return True
            else:
                return False
            
            
    def name_validate (self, action, value_if_allowed, text):
        if action == '1':  # insert
            if value_if_allowed == "Digite o nome do cliente":
                return True
            if value_if_allowed.isalpha():
                return True
            else:
                return False
            
            
    def city_validate(self, action, value_if_allowed, text):
        if action == '1': # insert
            if value_if_allowed == "Digite a cidade do cliente":
                return True
            if value_if_allowed.isalpha():
                return True
            else:
                return False
            
            
            
            