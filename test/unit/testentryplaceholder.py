import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.modules import Tk, pytest
from src.utils.placeholder import entryplaceholder

@pytest.fixture
def setup_entry():
    """ fixture para criar o ambiente de testes"""
    root = Tk()
    root.withdraw()
    entry = entryplaceholder(root, placeholder="Digite o nome", color="gray")
    yield entry, root
    root.destroy()
    
def test_placeholer_cleared_in_focus(setup_entry):
    """ Testa se o placeholder é removido quando o campo é focado """
    entry, root = setup_entry
    entry.focus_set()
    root.update()
    assert entry.get() == ""
    
def test_placeholder_restored_on_focus_out(setup_entry):
    """ Testa se o placeholder é restaurado quando o campo perde o foco """
    entry, root = setup_entry
    entry.focus_set()
    entry.focus_out()
    root.update_idletasks()
    assert entry.get() == "Digite o nome"
    
def test_get_value_with_user_input(setup_entry):
    """ Testa se o método get() retorna o valor do usuário """
    entry, root = setup_entry
    entry.focus_set()
    root.update()
    entry.insert(0, "User input")
    assert entry.get_value() == "User input"
    
def test_get_value_with_placeholder(setup_entry):
    """ Testa se o método get() retorna um valor vazio quando o placeholder está ativo """
    entry, root = setup_entry
    entry.focus_set()
    root.update_idletasks()
    assert entry.get_value() == ""
