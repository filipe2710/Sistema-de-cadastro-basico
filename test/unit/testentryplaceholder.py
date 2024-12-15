import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import unittest
from modules import Tk
from utils.placeholder import entryplaceholder


class TestEntryPlaceholder(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.entry = entryplaceholder(self.root, placeholder="Digite o nome")
        
    def tearDown(self):
        self.entry.destroy()
        self.root.destroy()
        
    def test_placeholder_cleared_on_focus(self):
        """Testa se o placeholder é removido ao ganhar foco."""
        self.entry.focus_set()  # Coloca o foco no widget
        self.entry.update_idletasks()  # Atualiza o estado do widget
        self.assertEqual(self.entry.get(), "")  # O placeholder deve ter sido removido

    def test_no_placeholder_restored_with_user_input(self):
        """Testa se o placeholder não é restaurado quando há texto do usuário."""
        self.entry.focus_set()  # Coloca o foco no widget
        self.entry.insert(0, "User input")
        self.entry.focus_out()  # Simula o foco novamente
        self.assertEqual(self.entry.get(), "User input")  # O texto do usuário deve ser preservado

    def test_get_value_with_user_input(self):
        """Testa se `get_value` retorna o valor inserido pelo usuário."""
        self.entry.focus_set()  # Coloca o foco no widget
        self.entry.insert(0, "User input")
        self.assertEqual(self.entry.get_value(), "User input")  # Deve retornar o texto do usuário

if __name__ == "__main__":
    unittest.main()