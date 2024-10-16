from tkinter import *
from tkinter import ttk

#JANELA TK <html>
root = Tk()

#TÍTULO DO APP <title>
root.title("Milhas para Kilomêtros")

def calculate(*args):
    try:
        value = float(milhas.get()) # ENTRADA
        result = int(value * 1.6) # PROCESSAMENTO
        kms.set (result) # SAÍDA
    except ValueError:
        pass

#CORPO DO APP <body>
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

milhas = StringVar()
milhas_entry = ttk.Entry(mainframe, width=7, textvariable=milhas)
milhas_entry.grid(column=2, row=1, sticky=(W, E))

kms = StringVar()
ttk.Label(mainframe, textvariable=kms).grid(column=2, row=2, sticky=(W, E))

#BOTÃO <button>
ttk.Button(mainframe, text="CALCULAR", command=calculate).grid(column=3, row=3, sticky=W)

#TEXTOS <p>
ttk.Label(mainframe, text="Milhas").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="É EQUIVALENTE A").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Kilometros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
milhas_entry.focus()
root.bind("<Return>", calculate)

#LOOP P/ RENDERIZAÇÃO INTERMITENTE
root.mainloop()
