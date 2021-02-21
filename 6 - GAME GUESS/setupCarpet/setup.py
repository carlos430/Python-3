import os
import platform

def clear():
    # Modulo para limpiar la pantalla.
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def typeNumber(mensaje):
    # Modulo para introducir un número.
    while True:
        try:
            numero = int(input(f"{mensaje}: "))
        
            return numero

        except ValueError:
            print("Error: Debe introducir un numero entero")

        print()

