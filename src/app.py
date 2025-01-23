#import pdb; pdb.set_trace()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from modules import *
    print("importado o modules com sucesso")
except:
    print("erro ao importar")
try:
    from utils.validatores import validators
    print("importado o validators com sucesso")
except:
    print("importado o validators com erro")
try:
    from utils.gradient import gradientframe
    print("importado o gradientframe com sucesso")
except:
    print("importado o gradientframe com erro")
try:
    from report import report
    print("importado o report com sucesso")
except:
    print("importado o report com erro")
try:
    from functions import functions
    print("importado o functions com sucesso")
except:
    print("importado o functions com erro")
try:
    from utils.placeholder import entryplaceholder
    print("importado o entryplaceholder com sucesso")
except:
    print("importado o entryplaceholder com erro")
try:
    from utils.form_handler import Form_handler
    print("importado o Form_handler com sucesso")
except: 
    print("importado o Form_handler com erro")
try:
    from utils.Format_entry import format_entry
    print("importado o format_entry com sucesso")
except: 
    print("importado o format_entry com erro")



# treinando com GUI no tkinter a primeira vez

# criando a intancia da janela principal do tkintes


# classe da application
class Application(functions, report, validators, format_entry):
    def __init__(self):  # funçãa metodo construtor init. com o parametro self
        self.root = Tk()  # colocando o tkintes em uma variavel
        self.screen()  # chamando a função screen (tela)
        self.frame_of_screen()  # chamando a função frame of screen (quadro de tela)
        self.creating_buttons()  # chamando a função criating buttons (criando botões)
        self.label_and_inputs()  # chamando a função label and inputs (rótulos e entradas)
        self.list_frame2()
        self.set_up_table()
        self.select_list()
        self.change_client()
        self.menus()
        self.root.mainloop()  # um loop de abertura ?
        
    def postal_code(self):
        self.cidade_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
            
        # Configurando a fonte antes de inserir os valores
        self.cidade_entry.config(font=("arial", 8,), fg="black")
        self.endereco_entry.config(font=("arial", 8,), fg="black")
        self.bairro_entry.config(font=("arial", 8,), fg="black")
        
        # Obtem o CEP do campo de entrada
        zipcode = self.cep_entry.get()
        
        # faz requisição para a API viacep
        try:
            response = requests.get(f"https://viacep.com.br/ws/{zipcode}/json/")
            if response.status_code == 200:
                datazipcode = response.json()
                if "erro" not in datazipcode:
                    self.cidade_entry.insert(0, datazipcode.get('localidade', ''))
                    self.endereco_entry.insert(0, datazipcode.get('logradouro', ''))
                    self.bairro_entry.insert(0, datazipcode.get('bairro', ''))
                else:
                    messagebox.showinfo("erro", "CEP não encontrado")
            else:
                messagebox.showinfo("erro", "CEP não encontrado")
        except Exception as e:
            print(f"An error occurred: {e}")

    def screen(self):  # fumção screen (janela)
        self.root.title("Primeira aplicação")  # titulo da aplicação
        self.root.configure(background="#3C36Eb")  # cos de fundo
        self.root.geometry(
            "600x500"
        )  # fazendo por padrão com que a janela fique 500x500
        self.root.resizable(width=True, height=False)  # não colocar outras dimenssões
        self.root.maxsize(width=1000, height=1000)  # o maximo de lagura e altura
        self.root.minsize(width=100, height=100)  # o minimo de largura e altura

    def frame_of_screen(self):  # função frame of screen (quadro de tela)
        self.frame1 = Frame(  # criando um quadro de tela
            self.root,  # colocando o quadro de tela na janela principal
            bd=4,  # borda do quadro de tela
            bg="#FAEBD7",  # cor de fundo do quadro
            highlightbackground="#4E82F2",  # cor de borda do quadro
            highlightthickness="3",  # o tamanho da borda
        )
        # a funçãa place permite que os elementos fique no lugar e o tamanho com a reponsividade em relação a x e y
        self.frame1.place(
            relx=0.03, rely=0.03, relwidth=0.94, relheight=0.46
        )  # relx e rely é o eixo que o elemento vai ficar e os relwidth e o relheight é o tamanho do elemento

        self.frame2 = Frame(
            self.root,
            bd=4,
            bg="#FAEBD7",
            highlightbackground="#4e81f2",
            highlightthickness="3",
        )
        self.frame2.place(relx=0.03, rely=0.5, relwidth=0.94, relheight=0.46)

    def creating_buttons(self):  # ? função criating buttons (criando botões)
        ''' podemo fazer moldura tambem ultilizando a função:
            self.canvas_bt = canvas(self.frame1, bd=, bg=,   highlightbackground=, highlightthickness=)        
            self.canva.place
        '''
        # criando abas no frama1
        self.abas_control = ttk.Notebook(self.frame1)
        self.aba1_control = gradientframe(self.abas_control)
        self.aba2_control = Frame(self.abas_control)
        self.aba1_control.configure(background="#fae8d7")
        self.aba2_control.configure(background="#fae8d7")
        self.abas_control.add(self.aba1_control, text="cadastro")
        self.abas_control.add(self.aba2_control, text="aba2")
        self.abas_control.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        # criando botão Limpar
        self.bt_limpar = Button(self.aba1_control, text="Limpa", bd=3, bg="#6197E8", fg="white", font=("arial", 8, "bold",),
            activebackground="#108ecb", # cor de fundo quando clica
            activeforeground="white",  # texto de fundo quando clica
            # comando que vai ser executado quando o botão for clicado
            command=self.clean_function,)
        # ? criando o botão limpar
        self.bt_limpar.place(relx=0.20, rely=0.15, relwidth=0.1, relheight=0.15) # colocando o botão limpar no frame1

        #criando um balão de texto no bt_novo
        '''text_ballon_clean = "Limpar campos"
        self.ballon_clean = tix.Balloon(self.frame1)
        self.ballon_clean.bind_widget(self.bt_limpar, balloonmsg=text_ballon_clean)''' # o tix esta indiponivel
        
        # criando botão buscar
        self.bt_buscar = Button(
            self.aba1_control,
            text="Buscar",
            bd=3,
            bg="#6197E8",
            fg="white",
            font=(
                "arial",
                8,
                "bold",
            ),
            activebackground="#108ecb", # cor de fundo quando clica
            activeforeground="white",  # texto de fundo quando clica

            command=self.seach,
            #command=self.root_2 # test
        )

        self.bt_buscar.place(relx=0.31, rely=0.15, relwidth=0.1, relheight=0.15) # colocando o botão buscar no frame1


        # criando botão novo
        self.bt_novo = Button(
            self.aba1_control,
            text="Novo",
            bd=3,
            bg="#6197E8",
            fg="white",
            font=(
                "arial",
                8,
                "bold",
            ),
            activebackground="#108ecb", # cor de fundo quando clica
            activeforeground="white",  # texto de fundo quando clica

            command=self.add_client,
        )

        self.bt_novo.place(relx=0.61, rely=0.15, relwidth=0.1, relheight=0.15) # colocando o botão novo no frame1

        # criando botão alterar
        self.bt_alterar = Button(
            self.aba1_control,
            text="Alterar",
            bd=3,
            bg="#6197E8",
            fg="white",
            font=(
                "arial",
                8,
                "bold",
            ),
            activebackground="#108ecb", # cor de fundo quando clica
            activeforeground="white",  # texto de fundo quando clica

            command=self.change_client,
        )

        self.bt_alterar.place(relx=0.72, rely=0.15, relwidth=0.1, relheight=0.15) # colocando o botão alterar no frame1

        # criando botão apagar
        self.bt_apagar = Button(
            self.aba1_control,
            text="Apagar",
            bd=3,
            bg="#6197E8",
            fg="white",
            font=(
                "arial",
                8,
                "bold",
            ),
            activebackground="#108ecb", # cor de fundo quando clica
            activeforeground="white",  # texto de fundo quando clica

            command=self.delete_client,
        )

        self.bt_apagar.place(relx=0.83, rely=0.15, relwidth=0.1, relheight=0.15)  # colocando o botão apagar no frame1
                
        # criando botão CEP
        self.bt_cep = Button(self.aba1_control, text="CEP", bd=3, bg="#e8f6f8", fg= "#6197e8", font=("arial", 8, "bold"), command=self.postal_code)
        
        self.bt_cep.place(relx=0.58, rely=0.35, relwidth=0.1, relheight=0.13)

    def label_and_inputs(self):  # função label and inputs (rótulos e entradas)
       # self.vality_entry(self.root)
        
        # criando label e inputs
        # codigo
        self.lb_codigo = Label(self.aba1_control, text="Código", bg="#FAEBD7", fg="#6197e8", font=("arial", 8))  # criando o rótulo codigo
        self.lb_codigo.place(relx=0.05, rely=0.08)  # colocando o rótulo codigo no frame1
        vcmd_id = self.root.register(self.codigo_validate)
        self.codigo_entry = entryplaceholder(self.aba1_control, placeholder="Id", font=("arial", 8), validatecommand=(vcmd_id, "%d", "%P", "%s"), validate="key")  # criando a entrada codigo
        self.codigo_entry.place(relx=0.05, rely=0.19, relwidth=0.1, relheight=0.10)  # colocando a entrada codigo no frame1t
        
        # nome
        self.lb_nome = Label(self.aba1_control, text="Nome", bg="#FAEBD7", fg="#6197e8", font=("arial", 8))
        self.lb_nome.place(relx=0.02, rely=0.35)
        vcmd_name = (self.root.register(self.name_validate))
        self.name_entry = entryplaceholder(self.aba1_control, placeholder="Digite o nome do cliente", color="gray", font=("arial", 8), validatecommand=(vcmd_name, "%d", "%P", "%s"), validate="key")
        self.name_entry.place(relx=0.09, rely=0.35, relwidth=0.45, relheight=0.10)
                
        # CEP
        vcmd_zip_code = self.root.register(self.zip_code_validate)
        self.cep_entry = entryplaceholder(self.aba1_control, placeholder="Digite o CEP do cliente", font=("arial", 8), validatecommand=(vcmd_zip_code, "%d", "%P", "%s"), validate="key")
        self.cep_entry.place(relx=0.7, rely=0.35, relwidth=0.25, relheight=0.10)

        # telefone
        self.lb_telefone = Label(self.aba1_control, text="Telefone", bg="#FAEBD7", fg="#6197e8", font=("arial", 8))
        self.lb_telefone.place(relx=0.05, rely=0.5)
        vcmd_phone = self.root.register(self.phone_validate)
        self.telefone_entry = entryplaceholder(self.aba1_control, placeholder="Digite o telefone do cliente", font=("arial", 8), validatecommand=(vcmd_phone, "%d", "%P", "%s"), validate="key")
        self.telefone_entry.bind("<KeyRelease>", lambda event: self.format_phone_number(event.widget)) # format phone
        self.telefone_entry.place(relx=0.15, rely=0.5, relwidth=0.35, relheight=0.10)

        # cidade
        self.lb_cidade = Label(self.aba1_control, text="Cidade", bg="#FAEBD7", fg="#6197e8", font=("arial", 8, "bold"))
        self.lb_cidade.place(relx=0.53, rely=0.5)
        vcmd_city = self.root.register(self.city_validate)
        self.cidade_entry = entryplaceholder(self.aba1_control, placeholder="Digite a cidade do cliente", font=("arial", 8), validatecommand=(vcmd_city, "%d", "%P", "%s"), validate="key")
        self.cidade_entry.place(relx=0.63, rely=0.5, relwidth=0.3, relheight=0.10)
        
        # endereço
        self.lb_endereco = Label(self.aba1_control, text="Endereço", bg="#FAEBD7", fg="#6197e8", font=("arial", 8))
        self.lb_endereco.place(relx=0.05, rely=0.65)
        vcmd_address = self.root.register(self.address_validate)
        self.endereco_entry = entryplaceholder(self.aba1_control, placeholder="Digite o seu endereço", font=("arial", 8, "bold"), validatecommand=(vcmd_address, "%d", "%P", "%s"), validate="key")
        self.endereco_entry.place(relx=0.15, rely=0.65, relwidth=0.3, relheight=0.10)
                
        # bairro
        self.lb_bairro = Label(self.aba1_control, text="Bairro", bg="#FAEBD7", fg="#6197e8", font=("arial", 8))
        self.lb_bairro.place(relx=0.53, rely=0.65)
        self.bairro_entry = entryplaceholder(self.aba1_control, placeholder="", font=("arial", 8, "bold"))
        self.bairro_entry.place(relx=0.63, rely=0.65, relwidth=0.3, relheight=0.10)

        # Drop down button
        self.lb_estado = Label(self.aba2_control, text="Estado Civil", bg="#FAE8D7", fg="#6197e8", font=("arial", 8, "bold"))
        self.lb_estado.place(relx=0.05, rely=0.08)

        self.tipvar = StringVar()
        self.tipvar.set("Solteiro(a)")
        self.drop = OptionMenu(self.aba2_control, self.tipvar, "Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viuvo(a)")
        self.drop.place(relx=0.03, rely=0.19, relwidth=0.20, relheight=0.1)
        self.estado_civil = self.tipvar.get()
        print(self.tipvar)

        self.bt_calendar = Button(self.aba2_control, text="Data", command=self.calendar)
        self.bt_calendar.place(relx=0.5, rely=0.10, relwidth=0.08)
        self.calendar_entry = Entry(self.aba2_control, width=10, font=("arial", 8)) 
        self.calendar_entry.place(relx=0.5, rely=0.25)

    def list_frame2(self):
        # Criando o Treeview com barra de rolagem
        self.listcli = ttk.Treeview(self.frame2, height=5, columns=("col1", "col2", "col3", "col4")) # criando o treeview (visualização em arvore)

        self.listcli.heading("#0", text="")
        self.listcli.heading("#1", text="Código")
        self.listcli.heading("#2", text="Nome")
        self.listcli.heading("#3", text="Telefone")
        self.listcli.heading("#4", text="Cidade")

        self.listcli.column("#0", width=1)
        self.listcli.column("#1", width=50)
        self.listcli.column("#2", width=125)
        self.listcli.column("#3", width=125)
        self.listcli.column("#4", width=100)

        self.listcli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollist = Scrollbar(
            self.frame2, orient="vertical", command=self.listcli.yview
        )
        self.scrollist.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        self.listcli.configure(yscrollcommand=self.scrollist.set)

        self.listcli.bind("<Double-1>", self.onclickdouble)

    def menus(self):
        style = ttk.Style()
        style.configure("TMenuButton", background="#808080", foreground="White")


        # Menu
        menubar = Menu(self.root, bg="#808080", fg="White", tearoff=0)
        self.root.config(menu=menubar)
        # Menu arquivo
        filemenu = Menu(menubar, tearoff=0, bg="#808080", fg="White")
        filemenu2 = Menu(menubar, tearoff=0, bg="#808080", fg="White")

        def quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Sobre", menu=filemenu2)

        filemenu.add_command(label="Sair", command= quit)
        filemenu.add_command(label="Limpar", command=self.clean_function)

        filemenu2.add_command(label="Ficha do cliente", command=self.generate_client_report)

    def root_2(self):
        self.root2 = Tk()
        self.root2.title("Relatório")
        self.root2.geometry("800x600")
        self.root2.resizable(False, False)
        self.root2.config(bg="#808080")
        self.root2.iconbitmap("icon.ico")
        self.root2.focus_force()
        self.root2.transient(self.root)
        self.root2.grab_set()

#   def vality_entry(self):
 #      self.vcmd2 = (self.root.register(self.validate_entry2), "%p")



Application()  # criando a aplicação
