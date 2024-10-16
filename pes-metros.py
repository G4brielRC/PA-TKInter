from tkinter import *
from tkinter import ttk

#JANELA TK <html>
root = Tk()

#TÍTULO DO APP <title>
root.title("Pés para Metros")

def calculate(*args):
    try:
        value = float(feet.get()) # ENTRADA
        result = int(0.3048 * value * 10000.0 + 0.5)/10000.0 # PROCESSAMENTO
        meters.set (result) # SAÍDA
    except ValueError:
        pass

#CORPO DO APP <body>
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

#BOTÃO <button>
ttk.Button(mainframe, text="CALCULAR", command=calculate).grid(column=3, row=3, sticky=W)

#TEXTOS <p>
ttk.Label(mainframe, text="PÉS").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="É EQUIVALENTE A").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="METROS").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)

#LOOP P/ RENDERIZAÇÃO INTERMITENTE
root.mainloop()
