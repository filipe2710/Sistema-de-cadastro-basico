
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from modules import *
from utils.form_handler import Form_handler
from utils.placeholder import entryplaceholder

# classe de fwnções(functions)
class functions(Form_handler):
    def __init__(self, master):
        # Inicialize os widgets placeholder
        self.name_entry = entryplaceholder(master, placeholder="Digite o nome do cliente", color="gray")
        self.telefone_entry = entryplaceholder(master, placeholder="Digite o telefone do cliente", color="gray")
        self.codigo_entry = entryplaceholder(master, placeholder="Digite o código do cliente", color="gray")
        self.cidade_entry = entryplaceholder(master, placeholder="Digite a cidade do cliente", color="gray")

    def clean_function(self): # função limpar
        # limpar os campos
        self.codigo_entry.delete(0, END) # deletando o texto do campo codigo_entry
        self.name_entry.delete(0, END) # deletando o texto do campo name_entry
        self.telefone_entry.delete(0, END) # deletando o texto do campo telefone_entry
        self.cidade_entry.delete(0, END) # deletando o texto do campo cidade_entry
        self.zip_code_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.bairro_entry.delete(9, END)

    def connect_bd(self): # função conectar a base de dados
        self.con = sqlite3.connect("clientes.bd") # conectando a base de dados
        self.cursor = self.con.cursor() # criando um cursor para a base de dados

    def disconnect_bd(self): # função desconectar a base de dados
        self.con.close() # desconectando a base de dados

    def variable(self): # função variável (variable)
         # guardando os dados importantes em uma variavel para otimizar tempo e linhas de codigo
        self.codigo = self.codigo_entry.get_value()
        self.nome = self.name_entry.get_value()
        self.telefone = self.telefone_entry.get_value()
        self.cidade = self.cidade_entry.get_value()

    def set_up_table(self): # função criar/configurar uma tabela (set up table)
        self.connect_bd() # conectando a base de dados
        print("conectando ao bd")  # printando na terminal
        self.cursor.execute( # executando a query
            """CREATE TABLE IF NOT EXISTS clientes (  -- criando a tabela
                            cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, -- codigo do cliente (obigatória) chave primaria
                            nome CHAR(50) NOT NULL,                         -- nome do cliente (obigatória)
                            telefone INTEaGER(20),                          -- telefone do cliente
                            cidade CHAR(50)                                 -- cidade do cliente
                            )
                            """
        )

        self.con.commit() # commitando a query
        print("BANCO DE DADOS CRIADO") # printando na terminal
        self.disconnect_bd() # desconectando a base de dados

    def add_client(self): # função adicionar cliente (add client)
        self.variable()
        if self.name_entry.get() == "":
            msg = "Para cadastrar um novo cliente é necessário \n"
            msg += "preencher o campo nome do cliente"
            messagebox.showerror("Erro", msg) # mensagem de erro
            return
        self.save_data()
        self.connect_bd()
        self.cursor.execute(
            """INSERT INTO clientes (nome, telefone, cidade) VALUES (?, ?, ?)""",  # inserindo os dados na tabela
            (self.nome, self.telefone, self.cidade), 
        )
        self.con.commit()
        self.disconnect_bd()
        self.select_list()
        self.clean_function()

        # Limpa todos os itens atuais no Treeview

    def select_list(self): # função selecionar lista (select list)
        self.listcli.delete(*self.listcli.get_children()) # deletando todos os itens da lista

        # Conecta ao banco de dados e busca os dados
        self.connect_bd()
        data = self.cursor.execute(
            """SELECT cod, nome, telefone, cidade FROM clientes
               ORDER BY nome ASC""" # ordenando a tabela pele o nome ascresente
        ).fetchall() # buscar dados

        # Insere os novos dados no Treeview
        for row in data:
            self.listcli.insert("", END, values=row)

        # Desconecta do banco de dados
        self.disconnect_bd()

    def onclickdouble(self, event): # função para quando o usuario clica duplo no item da lista (onclickdouble)
        self.clean_function()  # limpa os campos de entrada
        self.listcli.selection() # seleciona o item da lista

        for n in self.listcli.selection(): # percorre a lista
            col1, col2, col3, col4 = self.listcli.item(n, "values") # pega os valores da lista
            self.codigo_entry.insert(END, col1)
            self.name_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def delete_client(self): # função para deletar cliente (delete client)
        self.variable()
        self.connect_bd()
        self.cursor.execute(
            """DELETE FROM clientes WHERE cod = ?""", (self.codigo_entry.get(),)) # deletando o cliente

        self.con.commit()
        self.disconnect_bd()
        self.clean_function()
        self.select_list()

    def change_client(self): # função para alterar cliente (change client)
        self.variable()
        self.connect_bd()
        self.cursor.execute('''UPDATE clientes SET nome = ?, telefone = ?, cidade = ? WHERE cod = ?''',
                              (self.nome, self.telefone, self.cidade, self.codigo)) # alterando o cliente

        self.con.commit()
        self.disconnect_bd()
        self.clean_function()
        self.select_list()

    def seach(self): # função para buscar cliente (seach)
        self.connect_bd()
        self.listcli.delete(*self.listcli.get_children()) # deletando os dados da lista
        nome = self.name_entry.get() + '%'  # buscando o nome do cliente
        self.cursor.execute("""SELECT cod, nome, telefone, cidade FROM clientes WHERE nome LIKE ? ORDER BY nome ASC""", (nome, )) # buscando o nome do cliente
        data = self.cursor.fetchall() # buscando os dados
        for i in data: # percorrendo os dados
            self.listcli.insert("", END, values=i)
        self.clean_function()
        self.disconnect_bd()

    def calendar(self): # fv
        self.calendar1 = Calendar(self.aba2_control, fg="gray75", bg="blue", font=("Times", 5, "bold"), locale="pt_br")
        self.calendar1.place(relx=0.5, rely=0.1, relwidth= 0.3639, relheight=0.75)
        self.caldatestart = Button(self.aba2_control, text="Inserir data", command=self.print_date)
        self.caldatestart.place(relx=0.5, rely=0.87, relheight=0.1, relwidth=0.3639)
    
    def print_date(self):
        self.dateinsere = self.calendar1.get_date()
        self.calendar1.destroy()
        self.calendar_entry.delete(0, END)
        self.calendar_entry.insert(END, self.dateinsere)
        self.caldatestart.destroy()
