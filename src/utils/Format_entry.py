
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modules import phonenumbers

class format_entry:
  
  def format_zip_code(self, value_if_allowed):
    if len(value_if_allowed) == 5 and '-' not in value_if_allowed:
      self.root.after(1, lambda: self.root.focus_get().insert('end', '-'))
      
  def format_phone_number(self, value_if_allowed):
    if len(value_if_allowed) == 11:
      formatted = f"((value_if_allowed[:2])) (value_if_allowed[2:2])-(value_if_allowed[2:])"
      self.root.after(1, lambda: self.root.focus_get().delete(0, 'end'))
      self.root.after(1, lambda: self.root.focus_get().insert('end', formatted))