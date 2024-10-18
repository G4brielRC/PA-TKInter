from tkinter import *
from tkinter import ttk
import random
 
def gerar_senha():
   
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    caracteres= ['!', '@', '#', '$', '%', '&', '*', '£', '¢', '-', '_', '§']

    senha = ''
    for i in range(10):
        senha += random.choice(letras + numeros + caracteres)
  
    resultado.set(f'Senha Gerada: {senha}')



#JANELA TK
root = Tk()

#TÍTULO DO APP <title>
root.title("GERADOR DE SENHAS")

root.geometry("290x120")

#Variável para armazenar o resultado
resultado=StringVar()

#CORPO DO APP <body>
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#TEXTO que exibirá a senha gerada
senha_label = ttk.Label(mainframe, textvariable=resultado, font=('Tahoma', 14),foreground="ghostwhite", background='#4B0082')
senha_label.grid(column=3, row=4, sticky=(W, E))

#BOTÃO que chama a função para gerar a senha
gerar_button = ttk.Button(mainframe, text="Gerar Senha", command=gerar_senha)
gerar_button.grid(column=3, row=3, sticky=W)

style = ttk.Style()
style.configure('TButton', font=('Tahoma', 18, 'bold'), foreground='Navy', background='#000000', padding=10)
style.map('TButton', background=[('active', '#00FF00')])  
mainframe.configure(style='MainFrame.TFrame')

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#LOOP P/ RENDERIZAÇÃO INTERMITENTE
root.mainloop()