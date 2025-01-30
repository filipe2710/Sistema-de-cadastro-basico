
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
        if not self.get() and self.get() != self.placeholder:
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color
    
    # Remove o placeholder quando o usuário clica no campo
    def focus_in(self, *args):
        if self.get() == self.placeholder:  # Verifica se o texto atual é o placeholder
            self.delete(0, 'end')  # Limpa o campo
            self['fg'] = self.default_fg_color  # Restaura a cor original
    
    # Se o usuário sair do campo sem digitar nada, recoloca o placeholder
    def focus_out(self, *args):
        if not self.get():  # Se o campo estiver vazio
            self.put_place_holder()
    
    # Método que retorna o valor real do campo, sem o placeholder
    def get_value(self):
        value = self.get()
        if value == self.placeholder and self['fg'] == self.placeholder_color:
            return ''
        else:
            return value

    