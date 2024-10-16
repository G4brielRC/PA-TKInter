from tkinter import *
from tkinter import ttk

#JANELA TK <html>
root = Tk()

#TÍTULO DO APP <title>
root.title("Calcular IMC")

def calculate(*args):
    try:
       weight = float(peso.get()) # ENTRADA 1
       height = float(altura.get()) # ENTRADA 2 
       imc = weight / (height**2) # PROCESSAMENTO
       resultado.set(f"{imc :.2f}") # SAÍDA
    except ValueError:
       resultado.set("Erro")

#CORPO DO APP <body>
mainframe = ttk.Frame(root, padding="5 5 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

peso = StringVar()

peso_entry = ttk.Entry(mainframe, width=7, textvariable=peso)
peso_entry.grid(column=2, row=1, sticky=(W, E))

altura = StringVar()

altura_entry = ttk.Entry(mainframe, width=7, textvariable=altura)
altura_entry.grid(column=2, row=2, sticky=(W, E))

resultado = StringVar()
ttk.Label(mainframe, textvariable=resultado).grid(column=2, row=3, sticky=(W, E))  #resultado


#BOTÃO <button>
ttk.Button(mainframe, text="CALCULAR IMC ", command=calculate).grid(column=3, row=3, sticky=W)

#TEXTOS <p>
ttk.Label(mainframe, text="Peso").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Altura").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="IMC").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

    
peso_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
