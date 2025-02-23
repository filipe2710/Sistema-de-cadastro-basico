import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modules import pytest, Tk, Entry
from src.utils.validatores import validators
  
  
import pytest
from tkinter import Tk, Entry

@pytest.fixture  # Define a fixture para a criação dos entradas de teste
def setup_entries():
    window = Tk()
    window.withdraw()

    name_entry = Entry(window)
    phone_entry = Entry(window)
    codigo_entry = Entry(window)
    city_entry = Entry(window)
    zip_code_entry = Entry(window)
    address_entry = Entry(window)

    validatores = validators()
    yield validatores, name_entry, phone_entry, codigo_entry, city_entry, zip_code_entry, address_entry
    window.destroy()

def test_validators_name_validate_entry_char_and_space(setup_entries):
    validatores, name_entry, _, _, _, _, _ = setup_entries
    name_entry.insert(0, 'João')
    action = '1'
    value_if_allowed = name_entry.get()
    text = 'João'
    assert validatores.name_validate(action, value_if_allowed, text) is True

    name_entry.delete(0, 'end')
    name_entry.insert(0, ' João ')
    
    action = '1'
    value_if_allowed = name_entry.get()
    text = ' João '
    assert validatores.name_validate(action, value_if_allowed, text) is True

def test_validators_name_validate_entry_numeric_and_special_characters(setup_entries):
    validatores, name_entry, _, _, _, _, _ = setup_entries
    name_entry.insert(0, 'João123')
    action = '1'
    value_if_allowed = name_entry.get()
    text = 'João123'
    assert validatores.name_validate(action, value_if_allowed, text) is False

    name_entry.delete(0, 'end')  
    name_entry.insert(0, 'João@')
    
    action = '1'
    value_if_allowed = name_entry.get()
    text = 'João@'
    assert validatores.name_validate(action, value_if_allowed, text) is False

def test_validators_name_validate_entry_null(setup_entries):
    validatores, name_entry, _, _, _, _, _ = setup_entries
    name_entry.delete(0, 'end')
    action = '1'
    value_if_allowed = name_entry.get()
    text = ''
    assert validatores.name_validate(action, value_if_allowed, text) is True

def test_validators_name_validate_entry_value_equal_placeholder(setup_entries):
    validatores, name_entry, _, _, _, _, _ = setup_entries
    name_entry.insert(0, 'Digite o nome do cliente')
    action = '1'
    value_if_allowed = name_entry.get()
    text = 'Digite o nome do cliente'
    assert validatores.name_validate(action, value_if_allowed, text) is True

def test_validators_phone_validate_entry_format_value_valid(setup_entries):
    validatores, _, phone_entry, _, _, _, _ = setup_entries
    phone_entry.insert(0, '(11) 9999-9999')
    action = '1'
    value_if_allowed = phone_entry.get()
    text = '(11) 9999-9999'
    assert validatores.phone_validate(action, value_if_allowed, text) is True

def test_validators_phone_validate_entry_char_or_symbol_invalid(setup_entries):
    validatores, _, phone_entry, _, _, _, _ = setup_entries
    phone_entry.insert(0, '(11) 9999-999a')
    action = '1'
    value_if_allowed = phone_entry.get()
    text = '(11) 9999-999a'
    assert validatores.phone_validate(action, value_if_allowed, text) is False

    phone_entry.delete(0, 'end')
    phone_entry.insert(0, '(1#) 999*-99@9')
    
    action = '1'
    value_if_allowed = phone_entry.get()
    text = '(1#) 999*-99@9'
    assert validatores.phone_validate(action, value_if_allowed, text) is False

def test_validators_phone_validate_entry_insert_of_more_than_11_digits(setup_entries):
    validatores, _, phone_entry, _, _, _, _ = setup_entries
    phone_entry.insert(0, '(11) 9999-9999999999')
    action = '1'
    value_if_allowed = phone_entry.get()
    text = '(11) 9999-9999999999'
    assert validatores.phone_validate(action, value_if_allowed, text) is False

def test_validators_phone_validate_entry_correct_characters(setup_entries):
    validatores, _, phone_entry, _, _, _, _ = setup_entries
    phone_entry.insert(0, '(11) 9999-9999')
    action = '1'
    value_if_allowed = phone_entry.get()
    text = '(11) 9999-9999'
    phone_entry.delete(-1)
    assert validatores.phone_validate(action, value_if_allowed, text) is True

def test_validators_codigo_validate_entry_insert_only_numbers(setup_entries):
    validatores, _, _, codigo_entry, _, _, _ = setup_entries
    codigo_entry.insert(0, '123')
    action = '1'
    value_if_allowed = codigo_entry.get()
    text = '123'
    assert validatores.codigo_validate(action, value_if_allowed, text) is True

def test_validators_codigo_validate_entry_insert_character(setup_entries):
    validatores, _, _, codigo_entry, _, _, _ = setup_entries
    codigo_entry.insert(0, '123a')
    action = '1'
    value_if_allowed = codigo_entry.get()
    text = '123a'
    assert validatores.codigo_validate(action, value_if_allowed, text) is False

def test_validators_codigo_validate_entry_delete_characters(setup_entries):
    validatores, _, _, codigo_entry, _, _, _ = setup_entries
    codigo_entry.insert(0, '123')
    action = '1'
    value_if_allowed = codigo_entry.get()
    text = '123'
    codigo_entry.delete(-1)
    assert validatores.codigo_validate(action, value_if_allowed, text) is True

def test_validators_city_validate_entry_insert_char_and_space(setup_entries):
    validatores, _, _, _, city_entry, _, _ = setup_entries
    city_entry.insert(0, 'São Paulo')
    action = '1'
    value_if_allowed = city_entry.get()
    text = 'São Paulo'
    assert validatores.city_validate(action, value_if_allowed, text) is True

    city_entry.delete(0, 'end')
    city_entry.insert(0, 'São Paulo ')
    
    action = '1'
    value_if_allowed = city_entry.get()
    text = 'São Paulo '
    assert validatores.city_validate(action, value_if_allowed, text) is False

def test_validators_city_validate_entry_insert_number_and_symbol(setup_entries):
    validatores, _, _, _, city_entry, _, _ = setup_entries
    city_entry.insert(0, 'São Paulo123')
    action = '1'
    value_if_allowed = city_entry.get()
    text = 'São Paulo123'
    assert validatores.city_validate(action, value_if_allowed, text) is False

    city_entry.delete(0, 'end')
    city_entry.insert(0, 'São Paulo@')
    
    action = '1'
    value_if_allowed = city_entry.get()
    text = 'São Paulo@'
    assert validatores.city_validate(action, value_if_allowed, text) is False

def test_validators_city_validate_entry_placeholder_invalid(setup_entries):
    validatores, _, _, _, city_entry, _, _ = setup_entries
    city_entry.insert(0, 'Digite a cidade do cliente')
    action = '1'
    value_if_allowed = city_entry.get()
    text = 'Digite a cidade do cliente'
    assert validatores.city_validate(action, value_if_allowed, text) is True

def test_validators_zip_code_validate_entry_insert_zip_code_valid(setup_entries):
    validatores, _, _, _, _, zip_code_entry, _ = setup_entries
    zip_code_entry.insert(0, '01001-000')
    action = '1'
    value_if_allowed = zip_code_entry.get()
    text = '01001-000'
    assert validatores.zip_code_validate(action, value_if_allowed, text) is True

def test_validators_zip_code_validate_entry_insert_zip_code_no_hyphen(setup_entries):
    validatores, _, _, _, _, zip_code_entry, _ = setup_entries
    zip_code_entry.insert(0, '01001000')
    action = '1'
    value_if_allowed = zip_code_entry.get()
    text = '01001000'
    assert validatores.zip_code_validate(action, value_if_allowed, text) is True

def test_validators_zip_code_validate_entry_insert_char_or_symbol(setup_entries):
    validatores, _, _, _, _, zip_code_entry, _ = setup_entries
    zip_code_entry.insert(0, '01001-000a')
    action = '1'
    value_if_allowed = zip_code_entry.get()
    text = '01001-000a'
    assert validatores.zip_code_validate(action, value_if_allowed, text) is False

    zip_code_entry.delete(0, 'end')
    zip_code_entry.insert(0, '01001-000@')
    
    action = '1'
    value_if_allowed = zip_code_entry.get()
    text = '01001-000@'
    assert validatores.zip_code_validate(action, value_if_allowed, text) is False

def test_validators_zip_code_validate_entry_insert_of_more_than_9_digits(setup_entries):
    validatores, _, _, _, _, zip_code_entry, _ = setup_entries
    zip_code_entry.insert(0, '01001-000000000')
    action = '1'
    value_if_allowed = zip_code_entry.get()
    text = '01001-000000000'
    assert validatores.zip_code_validate(action, value_if_allowed, text) is False

def test_validators_address_validate_entry_insert_address_valid(setup_entries):
    validatores, _, _, _, _, _, address_entry = setup_entries
    address_entry.insert(0, 'Rua do cliente, 123')
    action = '1'
    value_if_allowed = address_entry.get()
    text = 'Rua do cliente, 123'
    assert validatores.address_validate(action, value_if_allowed, text) is True

def test_validators_address_validate_entry_insert_symbol(setup_entries):
    validatores, _, _, _, _, _, address_entry = setup_entries
    address_entry.insert(0, 'Rua do cliente, 123@')
    action = '1'
    value_if_allowed = address_entry.get()
    text = 'Rua do cliente, 123@'
    assert validatores.address_validate(action, value_if_allowed, text) is False

    address_entry.delete(0, 'end')
    address_entry.insert(0, 'Rua do cliente, 123#')
    
    action = '1'
    value_if_allowed = address_entry.get()
    text = 'Rua do cliente, 123#'
    assert validatores.address_validate(action, value_if_allowed, text) is False

def test_validators_address_validate_entry_placeholder_invalid(setup_entries):
    validatores, _, _, _, _, _, address_entry = setup_entries
    address_entry.insert(0, 'Digite o endereço do cliente')
    action = '1'
    value_if_allowed = address_entry.get()
    text = 'Digite o endereço do cliente'
    assert validatores.address_validate(action, value_if_allowed, text) is True

  
  
# pytest test/unit/testvalidatores.py -v  



  



