import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from modules import *

class gradientframe(tk.Canvas): # classe quadro gradiente (gradientframe), que é um root

    def __init__(self, parent, color1= "#c6ccff", color2= "gray34", **kwargs): # podemos colocar as cores diretamente no widgets
        """
        Método construtor init. Inicializa o root com um gradiente de cor.
        
        Parâmetros:
        parent (tkinter widget): O widget pai no qual o root será inserido.
        color1 (str): A cor inicial do gradiente, no formato hexadecimal.
        color2 (str): A cor final do gradiente, no formato hexadecimal.
        **kwargs: Argumentos adicionais que são passados para o construtor da classe base tk.Canvas.
        """
        super().__init__ (parent, **kwargs) # # Chama o construtor da classe base tk.Canvas com o widget pai e argumentos adicionais.
        self._color1 = color1 
        self._color2 = color2
        self.bind("<Configure>", self.draw_gradient)  # Vincula o evento <Configure> ao método draw_gradient, para desenhar o gradiente quando o root for redimensionado.

    def draw_gradient(self, event=None):
        """Desenha um fundo gradiente no root"""
        self.delete("gradient")
        # Obter a largura e a altura do root
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        # Obter os valores RGB das cores
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        # Calcular as razões de mudança para cada componente de cor
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        # Desenhar linha para fazer o efeito gradiente
        for i in range(limit):
            r = int(r1 + (i * r_ratio))
            g = int(g1 + (i * g_ratio))
            b = int(b1 + (i * b_ratio))
            color = "#%4.4x%4.4x%4.4x" % (r, g, b)
            self.create_line(i, 0, i, height, fill=color, tags=("gradient", ))
        
        self.lower("gradient") # Mover as linhas de gradiente para o fundo, atrás de outros elementos do root.

    

if __name__ == "__main__":  # se o script for executado diretamente (não importado como módulo), execute o seguinte código:
    root = tk.Tk()  # Cria uma janela principal (root)
    root.title("Gradiente")  # Define o título da janela
    gradient_widget = gradientframe(root, "#2171a2", "#57aea1")  # Passando root como o widget pai
    gradient_widget.pack(fill=tk.BOTH, expand=True)  # Coloca o root na janela e expande para ocupar toda a janela
    root.mainloop()  # Inicia a execução da janela principa