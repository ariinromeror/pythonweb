import tkinter as tk
from tkinter import messagebox
import math

# --- FUNCIONES DE LÓGICA ---
def click_boton(valor):
    """Añade el texto del botón a la pantalla"""
    actual = pantalla.get()
    pantalla.insert(tk.END, valor)

def borrar_pantalla():
    """Limpia toda la pantalla"""
    pantalla.delete(0, tk.END)

def calcular_resultado():
    """Realiza la operación matemática final"""
    try:
        # Reemplazamos símbolos visuales por símbolos que Python entiende
        ecuacion = pantalla.get()
        ecuacion = ecuacion.replace('^', '**')
        ecuacion = ecuacion.replace('π', str(math.pi))
        ecuacion = ecuacion.replace('e', str(math.e))
        
        # Diccionario con funciones matemáticas para que eval las reconozca
        funciones_permitidas = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'sqrt': math.sqrt, 'log': math.log10, 'pi': math.pi, 'e': math.e
        }
        
        resultado = eval(ecuacion, {"__builtins__": None}, funciones_permitidas)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Operación no válida.\nRevisa los paréntesis.")

# --- DISEÑO DE LA INTERFAZ ---
ventana = tk.Tk()
ventana.title("Calculadora Científica Pro")
ventana.geometry("400x550")
ventana.configure(bg="#1e1e1e") # Fondo oscuro tipo VS Code

# Pantalla (Donde se escriben los números)
pantalla = tk.Entry(ventana, font=("Consolas", 24), bg="#252526", fg="white", 
                   borderwidth=0, justify="right", insertbackground="white")
pantalla.pack(fill="both", padx=20, pady=30)

# Contenedor de botones
marco_botones = tk.Frame(ventana, bg="#1e1e1e")
marco_botones.pack(fill="both", expand=True, padx=10, pady=10)

# Lista de botones organizados por filas
# Nota: 'sqrt' es raíz, 'log' es logaritmo
botones = [
    ('sin(', 'cos(', 'tan(', 'log(', 'C'),
    ('(', ')', '^', 'sqrt(', '/'),
    ('7', '8', '9', '*', 'π'),
    ('4', '5', '6', '-', 'e'),
    ('1', '2', '3', '+', '='),
    ('0', '.', ' ', ' ', ' ')
]

# Crear los botones con un bucle
for fila_index, fila in enumerate(botones):
    for col_index, texto in enumerate(fila):
        if texto.strip() == "": continue # Saltar espacios vacíos
        
        # Color especial para el botón de borrar y el de igual
        color_fondo = "#333333"
        if texto == "=": color_fondo = "#007acc"
        if texto == "C": color_fondo = "#d13438"

        btn = tk.Button(marco_botones, text=texto, font=("Segoe UI", 12, "bold"),
                        bg=color_fondo, fg="white", borderwidth=0, 
                        width=6, height=2, activebackground="#505050")
        
        # Configurar qué hace el botón al hacer clic
        if texto == "=":
            btn.config(command=calcular_resultado)
        elif texto == "C":
            btn.config(command=borrar_pantalla)
        else:
            btn.config(command=lambda t=texto: click_boton(t))
            
        btn.grid(row=fila_index, column=col_index, padx=3, pady=3, sticky="nsew")

# Hacer que los botones se estiren parejo
for i in range(5):
    marco_botones.grid_columnconfigure(i, weight=1)
for i in range(6):
    marco_botones.grid_rowconfigure(i, weight=1)

ventana.mainloop()
