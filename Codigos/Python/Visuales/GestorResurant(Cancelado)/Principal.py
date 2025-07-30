from tkinter import *

#Iniciar Tkinter
app = Tk()
#Ajustes
app.geometry("1020x630+0+0") #Tamaño de la ventana
app.resizable(0, 0) #Evitar Maximizar
app.config(bg="cyan2") #Color de fondo
app.title("Gestor Restaurante Al Picor") #Título de la ventana

#Panel Superior
panel_superior = Frame(app, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
Etiqueta_Titulo = Label(panel_superior, text="Sistema De Facturación", font=("Dosis", 58), fg="azure4", bg = "cyan2", width=22 )
Etiqueta_Titulo.grid(row=0, column=0)

#Panel Izquierdo
panel_izquierdo = Frame(app, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", font=("Dosis", 19, "bold"), bd = 1, relief=FLAT ,fg = "azure4")
panel_comidas.pack(side=LEFT)

#Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"), bd = 1, fg = "azure4", relief=FLAT)
panel_bebidas.pack(side=LEFT)

#Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"), bd = 1, fg = "azure4", relief=FLAT)
panel_postres.pack(side=LEFT)

#Panel Costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#Panel Derecho
panel_derecho = Frame(app, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

#Panel Calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg="azure4")
panel_calculadora.pack()

#Panel Factura
panel_factura = Frame(panel_derecho, bd=1, relief=FLAT, bg="azure4")
panel_factura.pack()

#Panel Botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg="azure4")
panel_botones.pack(side=BOTTOM)

#Lista de Productos
Lista_Comida = ["Nachos\nGuacamole", "Nachos al\n pastor", "Nachos de\n pollo", "Nachos al\n picor", "Tacos al\n pastor", "Tacos al\n picor"]
Lista_Bebidas = ["Cerveza", "Tequila", "granizado", "Limonada","Agua\n Jamaica","Coka","Jugo","Vino","SODA"]
Lista_Postres = ["Flan", "Cheesecake", "Brownie", "Helado"]

Variable_Comida = []
Contador = 0
for Comida in Lista_Comida:
    Variable_Comida.append(IntVar())
    Comida = Checkbutton(panel_comidas, text=Comida, font=("Dosis", 16,"bold"), onvalue=1, offvalue=0, variable=Variable_Comida[Contador])
    Comida.grid(row=Contador, column=0, sticky="w")
    Contador += 1

Varibles_Bebida = []
Contador = 0
for Bebida in Lista_Bebidas:
    Varibles_Bebida.append(IntVar())
    Bebida = Checkbutton(panel_bebidas, text=Bebida, font=("Dosis", 16,"bold"), onvalue=1, offvalue=0, variable=Varibles_Bebida[Contador])
    Bebida.grid(row=Contador, column=0, sticky="w")
    Contador += 1

Variables_Postres = []
Contador = 0
for Postre in Lista_Postres:
    Variables_Postres.append(IntVar())
    Postre = Checkbutton(panel_postres, text=Postre, font=("Dosis", 16,"bold"), onvalue=1, offvalue=0, variable=Variables_Postres[Contador])
    Postre.grid(row=Contador, column=0, sticky="w")
    Contador += 1




#Evitar cierre de ventana
app.mainloop()