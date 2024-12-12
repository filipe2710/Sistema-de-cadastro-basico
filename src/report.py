

from modules import webbrowser, canvas, A4

class report: # classe relatorio (report)
    def print_client(self): # metodo print_client
        webbrowser.open("Cliente.pdf") # abrindo o browser ou um app que abre arquivos ().pdf)

    def generate_client_report(self): # função generate client report (gerar um relatorio do cliente) e não colocar a fumção no __init__
        # criando um objeto do tipo canvas
        c = canvas.Canvas("Cliente.pdf", pagesize=A4) # criando um objeto do tipo canvas
        # criando um objeto do tipo canvas
        c.setFont("Helvetica", 20) # fonte e o tamanho da font
        c.drawString(200, 800, "Relatório de Clientes")  # colocando o texto no relatorio
        c.setFont("Helvetica", 15) 
        
        codigoRel = self.codigo_entry.get() # pegando o valor do codigo_entry
        nomeRel = self.nome_entry.get() # pegando o valor do nome_entry
        telefoneRel = self.telefone_entry.get() # pegando o valor do telefone_entry
        cidadeRel = self.cidade_entry.get() # pegando o valor do cidade_entry

        c.setFont("Helvetica-Bold", 24)
        # drawString (desenho texto)
        c.drawString(200, 750, "Relatório de Clientes")
        c.setFont("Helvetica-Bold", 15)
        c.drawString(75, 700, "Código: " ) # colocando o texto no relatorio
        c.drawString(75, 650, "Nome: ")
        c.drawString(75, 600, "Telefone: ")
        c.drawString(75, 550, "Cidade: " )
        c.setFont("Helvetica", 15)
        c.drawString(136, 700, codigoRel)
        c.drawString(125, 650, nomeRel)
        c.drawString(140, 600, telefoneRel)
        c.drawString(135, 550, cidadeRel)

        ''' podemos fazer uma linha ou uma borda/moldura, usando a funçãa:
            c.rect(50, 50,  50,   50, fill=(true/false), stroke=(true/false))
                   x,  y, width. height
        '''

        c.showPage() # mostrando a pagina
        c.save()  # salvando o arquivo
        self.print_client() # chamando a função print_client para abrir o pdf gerado automaticamente      