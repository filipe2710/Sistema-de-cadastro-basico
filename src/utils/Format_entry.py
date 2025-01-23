
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modules import phonenumbers

class format_entry:
  
  def format_zip_code(self, value_if_allowed):
    if len(value_if_allowed) == 5 and '-' not in value_if_allowed:
      self.root.after(1, lambda: self.root.focus_get().insert('end', '-'))
      
  def format_phone_number(self, entry_widget):
    current_value = entry_widget.get()
    clean_value = current_value.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    
    if len(clean_value) == 2:
         formatted_value = f"({clean_value}"
    elif len(clean_value) <= 6:
        formatted_value = f"({clean_value[:2]}) {clean_value[2:]}"
    else:
        formatted_value = f"({clean_value[:2]}) {clean_value[2:7]}-{clean_value[7:]}"
        
    entry_widget.delete(0, 'end')
    entry_widget.insert('end', formatted_value)
    