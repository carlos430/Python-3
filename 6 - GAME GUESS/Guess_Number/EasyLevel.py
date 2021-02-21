import time
import random
from setupCarpet import setup

# Nivel fácil de adivinar el número dado aleatoriamente por la máquina 
# usando el modulo random para que la pc pueda elegir un número y asi el 
# jugador logre adivinarlo.

# Se utiliza el modulo time para medir el tiempo que el usuario toma
# para adivinar el número ya dado por la pc.

def easy():
    print("\t******** Nivel Facil ********")

    winnerCounter = 0
    lostCounter = 0
    
    salir = "si"
    while salir == "si":

        # Calculo del tiempo inicial.
        tiempoInicial = time.time()

        # random.randint() este toma un numero aleatorio dentro del rango del 1 al 6.
        machineChoice = random.randint(1,6)

        # En esta condicion se evalúa si el número elegido por la pc es un Par o Impar
        # para darle una pista al jugador.
        if machineChoice % 2 == 0:
            print("\nPISTAS: Es un numero par")

        else:
            print("\nPISTAS: Es un numero impar")

        print("\nAdivine un numero entre 1 y 6")

        playerNumber = setup.typeNumber("Adivine el numero: ")

        # Calculo final del tiempo para evaluar cuanto tardó el usuario en adivinar el número
        # round() redondea el tiempo y el cero es para dar número flotante (3.0).

        tiempoFinal = time.time()
        tiempoResult = round(tiempoFinal - tiempoInicial, 0)

        # Condición comparando el número dado por el usuario y el numero dado por la máquina
        if playerNumber == machineChoice:
            print("Felicidades, Adivinaste el numero (^_^)")

            # Condición que determina el tiempo tomado por el usuario para adivinar el número 
            if tiempoResult <= 3:
                print(f"ERES UN GENI@, Tu tiempo fue de: {tiempoResult} segundos (^_^)")

            else:
                print(f"DEBES MEJORAR, Tu tiempo fue de: {tiempoResult} segundos (~_~)")
            
            winnerCounter = winnerCounter + 1

        else:
            print(f"Perdiste, El numero era {machineChoice} (~_~)")

            lostCounter = lostCounter + 1

        salir = input('''¿Desear continuar jugando? 
                    1 - Si  
                    2 - No  ''').lower()

        if salir == "no":

            # Mostrar los número de aciertos y desaciertos del usuario.
            print(f"\nNumeros de aciertos: {winnerCounter} ")
            print(f"Numeros de desaciertos: {lostCounter}\n")
            input("Presione Enter para continuar....")
            break
