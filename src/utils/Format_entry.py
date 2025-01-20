

class format_entry:
  
  def format_zip_code(self, value_if_allowed):
    if len(value_if_allowed) == 5 and '-' not in value_if_allowed:
      self.root.after(1, lambda: self.root.focus_get().insert('end', '-'))