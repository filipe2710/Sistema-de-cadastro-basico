import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modules import pytest, Tk, Entry
from src.utils.form_handler import Form_handler

@pytest.fixture
def setup_entries():
  # Create a Tkinter window
  window = Tk()
  window.withdraw()
  
  # Create form handler
  name_entry = Entry(window)
  telefone_entry = Entry(window)
  codigo_entry = Entry(window)
  cidade_entry = Entry(window)
  
  # Create a name entry widget
  form_handler = Form_handler(name_entry, telefone_entry, codigo_entry, cidade_entry)
  yield form_handler, name_entry, telefone_entry, codigo_entry, cidade_entry
  # Close the window
  window.destroy()
  
def test_form_handler_entry_null(setup_entries):
  form_handler, name_entry, _, _, _ = setup_entries
  assert form_handler.get_entry_value(name_entry) == ''
  
def test_form_handler_entry_blank(setup_entries):
  form_handler, name_entry, _, _, _ = setup_entries
  name_entry.insert(0, ' ')
  assert form_handler.get_entry_value(name_entry) == ''
  
def test_form_handler_entry_Placeholders_not_removed_correctly(setup_entries):
  form_handler, name_entry, _, _, _ = setup_entries
  name_entry.insert(0, ' Digite o nome do cliente ')
  assert form_handler.get_entry_value(name_entry) == ''
    
def test_form_handler_entry_excessively_long(setup_entries):
  '''  O que acontece se o nome, cidade ou telefone forem muito longos?'''
  form_handler, name_entry, telefone_entry, codigo_entry, _ = setup_entries
  name_entry.insert(0, 'a' * 1000)
  assert form_handler.get_entry_value(name_entry) == 'a' * 1000
  telefone_entry.insert(0, '1' * 1000)
  assert form_handler.get_entry_value(telefone_entry) == '1' * 1000
  codigo_entry.insert(0, '1' * 1000)
  assert form_handler.get_entry_value(codigo_entry) == '1' * 1000
  
def test_form_handler_entry_value_none(setup_entries):
  ''' O que acontece se tentarmos pegar um valor de entrada que não existe?'''
  form_handler, _, _, _, _ = setup_entries
  assert form_handler.get_entry_value(None) is None
  
def test_form_handler_save_data(setup_entries):
  form_handler, name_entry, telefone_entry, codigo_entry, cidade_entry = setup_entries
  name_entry.insert(0, 'joão')
  telefone_entry.insert(0, '11987654321')
  codigo_entry.insert(0, '123')
  cidade_entry.insert(0, 'São Paulo')
  
  form_handler.save_data()
  
  assert form_handler.name == 'joão'
  assert form_handler.telefone == '11987654321'
  assert form_handler.codigo == '123'
  assert form_handler.cidade == 'São Paulo'
  
  
# pytest test/unit/testformhandler.py -v  

  

  