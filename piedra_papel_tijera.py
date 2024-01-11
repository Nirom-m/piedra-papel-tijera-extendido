import tkinter as tk
from tkinter import messagebox
import random

# Definición de elementos
BASIC_MOVEMENTS = ["piedra", "papel", "tijera"]
ESPECIAL_MOVEMENTS = ["fuego", "agua", "rayo"]

COMBINED_MOVEMENTS = {
    ("piedra", "fuego"): "dragon",
    ("piedra", "agua"): "lodo",
    ("piedra", "rayo"): "chispa",
    ("papel", "fuego"): "ceniza",
    ("papel", "agua"): "humedad",
    ("papel", "rayo"): "pergamino",
    ("tijera", "fuego"): "atomic",
    ("tijera", "agua"): "presion",
    ("tijera", "rayo"): "estruendo",
}

# Definición de combinaciones que derrotan a sus contrarios
COMBINED_VICTORIES = {
    "dragon": ["lodo", "presion", "estruendo"],
    "chispa": ["ceniza", "pergamino", "estruendo"],
    "pergamino": ["humedad", "atomic", "lodo"],
    "atomic": ["presion", "estruendo", "pergamino"],
    "estruendo": ["chispa", "lodo", "atomic"],
    "lodo": ["pergamino", "dragon", "ceniza"],
    "presion": ["atomic", "dragon", "ceniza"],
    "ceniza": ["chispa", "lodo", "pergamino"],
    "humedad": ["ceniza", "presion", "estruendo"],
}

# Función para determinar el movimiento combinado del jugador1
def obtener_movimiento_combinado(movimiento_basico, movimiento_especial):
    return COMBINED_MOVEMENTS.get((movimiento_basico, movimiento_especial), None)

# Función para determinar el ganador entre dos movimientos
def determinar_ganador(movimiento1, movimiento2):
    if movimiento1 == movimiento2:
        return "Empate, ¡Vamos! vas a dejar que una ojalata este a tu nivel?!. Vos desempataras, lo se!"
    elif movimiento2 in COMBINED_VICTORIES.get(movimiento1, []):
        return "¡Gana el Jugador!, Excelente estrategia, sabía que lo lograrías!"
    elif movimiento1 in COMBINED_VICTORIES.get(movimiento2, []):
        return "¡Gana la I.A... FATALITY!, será en una próxima..."
    else:
        return "Sin ganador... por ahora"

# Función para manejar el clic del botón de movimiento básico
def seleccionar_movimiento_basico(movimiento):
    label_movimiento_basico.config(text=f"Jugador 1 eligió: {movimiento}")
    ventana.update_idletasks()

# Función para manejar el clic del botón de movimiento especial
def seleccionar_movimiento_especial(movimiento):
    label_movimiento_especial.config(text=f"Jugador 1 eligió: {movimiento}")
    ventana.update_idletasks()

# Función para manejar el clic del botón para calcular el resultado
def calcular_resultado():
    movimiento_basico_P1 = label_movimiento_basico.cget("text").split()[-1].lower()
    movimiento_especial_P1 = label_movimiento_especial.cget("text").split()[-1].lower()

    # Validación de la entrada del jugador 1
    if movimiento_basico_P1 not in BASIC_MOVEMENTS or movimiento_especial_P1 not in ESPECIAL_MOVEMENTS:
        messagebox.showwarning("Error", "Entrada no válida. Asegúrate de elegir movimientos básicos y especiales correctos.")
    else:
        # Obtención del movimiento combinado resultante
        combined_movement_P1 = obtener_movimiento_combinado(movimiento_basico_P1, movimiento_especial_P1)

        # Resultado
        if combined_movement_P1:
            label_resultado.config(text=f"Jugador 1 eligió: {combined_movement_P1} + {movimiento_especial_P1} = {combined_movement_P1}")
            movimiento_jugador2 = random.choice(list(COMBINED_MOVEMENTS.values()))
            label_resultado_IA.config(text=f"I.A. eligió: {movimiento_jugador2}")

            ganador = determinar_ganador(combined_movement_P1, movimiento_jugador2)
            label_ganador.config(text=f"{ganador}")

# Creación de la ventana
ventana = tk.Tk()
ventana.geometry("1000x400")
ventana.title("Juego Piedra, Papel, Tijera Extendido")

# Creación de widgets
label_movimiento_basico = tk.Label(ventana, text="Jugador 1 - Movimiento basico -", font=("Helvetica", 12))
label_movimiento_especial = tk.Label(ventana, text="Jugador 1 - Movimiento especial: -", font=("Helvetica", 12))
botones_basico = [tk.Button(ventana, text=movimiento, command=lambda m=movimiento: seleccionar_movimiento_basico(m), font=("Helvetica", 10)) for movimiento in BASIC_MOVEMENTS]
botones_especial = [tk.Button(ventana, text=movimiento, command=lambda m=movimiento: seleccionar_movimiento_especial(m), font=("Helvetica", 10)) for movimiento in ESPECIAL_MOVEMENTS]
boton_calcular = tk.Button(ventana, text="Calcular Resultado", command=calcular_resultado, font=("Helvetica", 12, "bold"))
label_resultado = tk.Label(ventana, text="", font=("Helvetica", 12, "italic"))
label_resultado_IA = tk.Label(ventana, text="", font=("Helvetica", 12, "italic"))
label_ganador = tk.Label(ventana, text="", font=("Helvetica", 14, "bold"))

# Posicionamiento de widgets
label_movimiento_basico.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")
label_movimiento_especial.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

for i, boton in enumerate(botones_basico):
    boton.grid(row=2, column=i, padx=5, pady=5, sticky="nsew")

for i, boton in enumerate(botones_especial):
    boton.grid(row=3, column=i, padx=5, pady=5, sticky="nsew")

boton_calcular.grid(row=4, column=0, columnspan=3, pady=10, sticky="nsew")
label_resultado.grid(row=5, column=0, columnspan=3, pady=10, sticky="nsew")
label_resultado_IA.grid(row=6, column=0, columnspan=3, pady=10, sticky="nsew")
label_ganador.grid(row=7, column=0, columnspan=3, pady=10, sticky="nsew")

# Configurar el sistema de gestión de geometría para centrar los widgets
for i in range(8):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(3):
    ventana.grid_columnconfigure(i, weight=1)

# Iniciar la aplicación
ventana.mainloop()
