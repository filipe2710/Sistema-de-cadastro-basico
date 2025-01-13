
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tkinter import Entry, Tk, Button


class entryplaceholder(Entry):
    def __init__(self, master=None, placeholder='PLACEHOLDER', color='gray', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']  # Salva a cor padrão do texto
        
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)
        
        self.put_place_holder()
    
    # Adiciona o placeholder e altera a cor do texto para a cor do placeholder
    def put_place_holder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
    
    # Remove o placeholder quando o usuário clica no campo
    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:  # Verifica se o texto atual é o placeholder
            self.delete(0, 'end')  # Limpa o campo
            self['fg'] = self.default_fg_color  # Restaura a cor original
    
    # Se o usuário sair do campo sem digitar nada, recoloca o placeholder
    def focus_out(self, *args):
        if not self.get():  # Se o campo estiver vazio
            self.put_place_holder()
    
    # Método que retorna o valor real do campo, sem o placeholder
    def get_value(self):
        if self['fg'] == self.placeholder_color:
            return ''
        else:
            return self.get()

def telefone_validate(value_if_allowed):
    # A função deve validar apenas números
    if value_if_allowed.isdigit() or value_if_allowed == "":
        return True
    return False  # Bloqueia a inserção de caracteres não numéricos


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300")
    root.title("Teste Entry com Placeholder")

    # Campo com placeholder e validação de telefone
    entry_validated = entryplaceholder(
        root,
        placeholder="Digite o telefone",
        color="gray",
        validate_cmd=telefone_validate,  # Validação de telefone
    )
    entry_validated.pack(pady=20)

    # Campo sem validação
    entry_no_validation = entryplaceholder(
        root,
        placeholder="Digite algo aqui...",
        color="gray"
    )
    entry_no_validation.pack(pady=20)

    # Botão para obter valores dos campos
    def show_values():
        print(f"Telefone: '{entry_validated.get_value()}'")
        print(f"Outro Campo: '{entry_no_validation.get_value()}'")

    btn = Button(root, text="Mostrar Valores", command=show_values)
    btn.pack(pady=20)

    root.mainloop()