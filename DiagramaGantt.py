import os
import matplotlib.pyplot as plt
from colorama import init, Fore, Style
init()

# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')

# Presentación
print("\033[38;2;100;200;255m" + """
=======================================
    GENERADOR DE DIAGRAMA DE GANTT
=======================================
""" + "\033[0m")

print("""
Este proyecto permite crear fácilmente diagramas de Gantt personalizados desde la línea de comandos,\nsin necesidad de hojas de cálculo ni herramientas gráficas complejas.

A través de una interfaz textual clara y amigable, puedes introducir el nombre y duración de cada etapa de un proyecto. \nEl script genera automáticamente un gráfico visual en formato PNG, con el nombre que tu le des.

Ideal para estudiantes, planificadores de proyectos o cualquier persona que necesite visualizar tareas y tiempos de ejecución\nde forma rápida y elegante, directamente desde la terminal.
""")

print()


# Paso 1: Solicitar información al usuario
num_etapas = int(input("\033[38;2;255;255;0m¿Cuántas etapas tiene el proyecto?: \033[0m"))
print()

etapas = []
inicios = []
fines = []

for i in range(num_etapas):
    nombre = input(f"{Fore.CYAN}Nombre de la etapa {i+1}: {Style.RESET_ALL}")

    while True:
        try:
            inicio = int(input(f"Semana de inicio de '{nombre}': "))
            fin = int(input(f"Semana de fin de '{nombre}': "))
            if inicio <= 0 or fin <= 0:
                print("⚠️ Las semanas deben ser mayores que 0. Intente de nuevo.")
                continue
            if inicio > fin:
                print("⚠️ La semana de inicio no puede ser mayor que la de fin. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("⚠️ Por favor, introduzca un número entero válido.")
    etapas.append(nombre)
    inicios.append(inicio)
    fines.append(fin)
    print("-" * 40)

# Nombre del archivo de salida
print()
output_file = input("\033[38;2;255;255;0mNombre del archivo de salida (sin extensión): \033[0m").strip()

# Paso 2: Calcular duraciones
duraciones = [fin - inicio + 1 for inicio, fin in zip(inicios, fines)]

# Paso 3: Crear diagrama de Gantt
fig, ax = plt.subplots(figsize=(10, 5))

# Invertir el orden de las etapas para que la primera aparezca arriba
etapas_reverso = etapas[::-1]
inicios_reverso = inicios[::-1]
duraciones_reverso = duraciones[::-1]

for i in range(num_etapas):
    ax.barh(etapas_reverso[i], duraciones_reverso[i], left=inicios_reverso[i] - 1, edgecolor='black', align='center')

# Estilo del gráfico
ax.set_xlabel("Semanas")
ax.set_title("Diagrama de Gantt del Proyecto")
ax.set_xlim(0, max(fines) + 1)
ax.set_xticks(range(0, max(fines) + 2))
ax.set_xticklabels([str(i) for i in range(0, max(fines) + 2)])
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Guardar y mostrar
plt.tight_layout()
plt.savefig(f"{output_file}.png", format='png', dpi=300)
plt.show()
print(f"\nDiagrama guardado como '{output_file}.png'")
