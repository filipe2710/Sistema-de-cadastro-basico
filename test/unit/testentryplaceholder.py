import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.modules import Tk
from src.utils.placeholder import entryplaceholder

def main():
    root = Tk()
    root.geometry("300x200")

    nome_entry = entryplaceholder(root, placeholder="Digite o nome", color="gray")
    nome_entry.pack(pady=5)
    
    telefone_entry = entryplaceholder(root, placeholder="Digite o telefone", color="gray")
    telefone_entry.pack(pady=5)
    
    cidade_entry = entryplaceholder(root, placeholder="Digite a cidade", color="gray")
    cidade_entry.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
