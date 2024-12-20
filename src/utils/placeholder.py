
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tkinter import Entry, Tk


class entryplaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color="gray", *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"] if "fg" in kwargs else "black"
        self.is_placeholder_visible = True  # Estado do placeholder

        self.put_placeholder()

        # Vincular eventos
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

    def put_placeholder(self):
        """Exibe o placeholder no campo."""
        if self.get().strip() == "":
            self.is_placeholder_visible = True
            self.delete(0, "end")
            self.insert(0, self.placeholder)
            self["fg"] = self.placeholder_color

    def remove_placeholder(self):
        """Remove o placeholder."""
        if self.is_placeholder_visible:
            self.is_placeholder_visible = False
            self.delete(0, "end")
            self["fg"] = self.default_fg_color

    def focus_in(self, *args):
        """Evento ao ganhar foco."""
        self.remove_placeholder()

    def focus_out(self, *args):
        """Evento ao perder foco."""
        if not self.get().strip():  # Recoloca o placeholder se o campo estiver vazio
            self.put_placeholder()

    def get_value(self):
        """Retorna o valor real do campo, ignorando o placeholder."""
        if self.is_placeholder_visible:
            return ""
        return super().get()


# Exemplo de uso
if __name__ == "__main__":
    root = Tk()
    root.geometry("300x200")
    entry = entryplaceholder(root, placeholder="Digite algo...", color="gray")
    entry.pack()
    root.mainloop()