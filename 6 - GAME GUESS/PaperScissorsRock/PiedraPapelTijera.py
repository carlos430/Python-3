import time
import random

# Este modulo consiste en el juego de Piedra, Papel y Tijera donde la máquina 
# selecciona un elemento de manera aleatoria de la lista.

# Se utiliza el modulo time para medir el tiempo que el usuario toma
# para adivinar el jugador ya dado por la pc.

def piedra_papel_tijera():
    
    print("\t******** Piedra Paper Tijera ********")
    
    winnerCounter = 0
    lostCounter = 0

    salir = "si"

    while salir == "si":

        machineList = ["Piedra", "Papel", "Tijera"]

        # random.choice() este toma un elemento aleatoriamente que esta dentro de la lista.
        playerChoice = input("\nPiedra Papel o Tijera: ").capitalize()

        # Condicionales para evaluar el elemento escogido por el usuario
        # si esta en la lista se continua con la operación sino devuelve un mensaje
        # de que lo escrito no esta en la lista.
        if playerChoice not in machineList:
            print("No hagas Trampas (*_*)")
            continue

        # La maquina hace su selección tomandose un tiempo de 0.5 segundos.
        machineChoice = random.choice(machineList).capitalize()
        time.sleep(0.5)
        print(f"La Computadora eligió {machineChoice}\n")

        # Condiciones para evaluar lo escogido por el usuario y lo escogido por la máquina.
        if playerChoice == machineChoice:
            print("Hubo un empate")

        elif playerChoice == "Piedra" and machineChoice == "Tijera":
            print("\nGanaste")

            winnerCounter = winnerCounter + 1

        elif playerChoice == "Tijera" and machineChoice == "Papel":
            print("\nGanaste")

            winnerCounter = winnerCounter + 1

        elif playerChoice == "Papel" and machineChoice == "Piedra":
            print("\nGanaste")

            winnerCounter = winnerCounter + 1

        else:
            print("Perdiste")

            lostCounter = lostCounter + 1

        salir = input('''Deseas continuar jugando?
                    [1] - Si
                    [2] - No ''')

        if salir == "no":
            
            # Mostrar los número de aciertos y desaciertos del usuario.
            print(f"\nNumeros de aciertos: {winnerCounter} ")
            print(f"Numeros de desaciertos: {lostCounter}\n")
            input("Presione Enter para continuar....")
            break