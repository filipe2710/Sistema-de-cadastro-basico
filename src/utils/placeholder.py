

from src.modules import *


class entryplaceholder(Entry):
  def __init__(self, master= None, placeholder= 'PLACEHOLDER', color= 'gray', *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    
    self.placeholder = placeholder
    self.placeholder_color = color
    self.default_fg_color = self['fg']
    
    self.bind("<FocusIn>", self.focus_in)
    self.bind("<FocusOut>", self.focus_out)
    
    self.put_place_holder()
    
  def put_place_holder(self):
    self.insert(0, self.placeholder)
    self['fg'] = self.placeholder_color
    
  def focus_in(self, *args):
    if self['fg'] == self.placeholder_color:
      self.delete('0', 'end')
      self['fg'] = self.default_fg_color
      
  def focus_out(self, *args):
    if not self.get():
      self.put_place_holder()
      
  def get_value(self):
    if self['fg'] == self.placeholder_color:
      return ''
    else:
      return self.get()
      
      

# Testando a classe EntryPlaceholder
if __name__ == "__main__":
    root = Tk()
    entry = entryplaceholder(root, placeholder="Digite algo...", color="gray")
    entry.pack(pady=10, padx=10)
    root.mainloop()
