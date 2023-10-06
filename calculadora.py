import tkinter as tk
import customtkinter

customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("800+350")
app.title("Calculadora")

entrada_texto = tk.StringVar()
entrada_texto.set("")

def agregar_caracter(caracter):
    if caracter == 'AC':
        entrada_texto.set("")
    else:
        entrada_actual = entrada_texto.get()
        entrada_texto.set(entrada_actual + caracter)

def calcular():
    try:
        entrada_actual = entrada_texto.get()
        resultado = str(eval(entrada_actual))
        entrada_texto.set(resultado)
    except:
        entrada_texto.set("Error")

# Crear un Frame para los botones de la calculadora
frame_botones = tk.Frame(app, padx=10, pady=5)
frame_botones.grid(row=1, column=0, columnspan=1)

# Crear botones numéricos y de operaciones en el Frame
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'AC'
]

fila = 0
columna = 0

for boton_texto in botones:
    if boton_texto == '=':
        customtkinter.CTkButton(
            master=frame_botones, 
            text=boton_texto, 
            command=calcular, 
            width=45, 
            height=45, 
            border_width=1,
            font=("Helvetica", 20)).grid(row=fila, column=columna)
    else:
        customtkinter.CTkButton(
            master=frame_botones,
            text=boton_texto, 
            command=lambda bt=boton_texto: agregar_caracter(bt), 
            width=45, 
            height=45, 
            border_width=1, 
            font=("Helvetica", 20)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

entry = customtkinter.CTkEntry(app, textvariable=entrada_texto, width=180, height=40, border_width=3, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)

app.mainloop()
