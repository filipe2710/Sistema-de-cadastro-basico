
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tkinter import Entry, Tk, Button


class entryplaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color="gray", validate_cmd=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = kwargs.get("fg", "black")
        self.is_placeholder_visible = False  # Inicialmente o placeholder não está visível
        self.validate_cmd = validate_cmd  # Validação personalizada
        self.put_placeholder()

        # Vincular eventos de foco
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        # Configurar a validação
        if validate_cmd:
            self.config(validate="key", validatecommand=(self.register(self.validate_entry), "%P"))

    def put_placeholder(self):
        """Exibe o placeholder no campo se ele estiver vazio."""
        if not self.get().strip():  # Só insere o placeholder se o campo estiver vazio
            self.is_placeholder_visible = True
            self.delete(0, "end")
            self.insert(0, self.placeholder)
            self["fg"] = self.placeholder_color

    def remove_placeholder(self):
        """Remove o placeholder se ele estiver visível."""
        if self.is_placeholder_visible:
            self.is_placeholder_visible = False
            self.delete(0, "end")
            self["fg"] = self.default_fg_color

    def focus_in(self, *args):
        """Evento ao ganhar foco no campo."""
        self.remove_placeholder()

    def focus_out(self, *args):
        """Evento ao perder foco no campo."""
        if not self.get().strip():  # Se o campo estiver vazio, o placeholder volta
            self.put_placeholder()

    def validate_entry(self, value_if_allowed):
        """Executa a validação personalizada, ignorando o placeholder."""
        if self.is_placeholder_visible:
            return True  # Ignorar validação se o placeholder está visível
        if self.validate_cmd:
            return self.validate_cmd(value_if_allowed)
        return True

    def get_value(self):
        """Retorna o valor real do campo, ignorando o placeholder."""
        if self.is_placeholder_visible:
            return ""
        return super().get()


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