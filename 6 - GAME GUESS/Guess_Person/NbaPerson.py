import time 
import random

# Este modulo consiste en adivinar el jugador de la NBA dado aleatoriamente por la máquina 
# usando el modulo random para que la pc pueda elegir un jugador y asi el 
# jugador logre adivinarlo.

# Se utiliza el modulo time para medir el tiempo que el usuario toma
# para adivinar el jugador ya dado por la pc.

def nba_player():
    print("\t******** Nivel NBA ********")

    winnerCounter = 0
    lostCounter = 0

    salir = "si"
    while salir == "si":

        # Listado general de los jugadores y en esta lista la máquina escogerá un jugador de manera aleatoria.
        playerNba = ["Kevin Durant", "Stephen Curry", "Lebron James", "Paul George", "John Wall"
                    "Kyrie Irving",  "Draymon Green", "Antony Davis", "Kawhi Leonard", "James Harden",              
                    "DeAndre Jordan","Klay Thompson", "Alex Caruso",  "Patrick Beverley", "Eric Gordon"]

        # Calculo del tiempo inicial
        tiempoInicial = time.time()

        # random.choice() este toma un jugador aleatoriamente que esta dentro de la lista general del jugadores.
        machineChoice = random.choice(playerNba).upper()

        # Conjunto de lista de equipos de la NBA donde pertenece los jugadores
        # para darle una pista al jugador. 
        BrooklynList = ["KEVIN DURANT", "KYRIE IRVING", "DEANDRE JORDAN"]
        GsWarriorsList = ["STEPHEN CURRY", "DRAYMON GREEN", "KLAY THOMPSON"]
        LakersList = ["LEBRON JAMES", "ANTONY DAVIS", "ALEX CARUSO"]
        ClippersList = ["PAUL GEORGE", "KAWHI LEONARD", "PATRICK BEVERLEY"]
        HoustonList = ["JOHN WALL", "JAMES HARDEN", "ERIC GORDON"]

        # Condiciones para evaluar a que equipo pertenece el jugador seleccionado por la máquina
        # y darle una pista al jugador.
        if machineChoice in BrooklynList:
            print("PISTAS: Puede ser uno de estos jugadores")
            for indice, BrooklynPlayer in enumerate(BrooklynList, 1):
                print(indice, BrooklynPlayer)
        
        if machineChoice in GsWarriorsList:
            print("PISTAS: Puede ser uno de estos jugadores")
            for indice, GsWarriorsPlayer in enumerate(GsWarriorsList, 1):
                print(indice, GsWarriorsPlayer)
        
        if machineChoice in LakersList:
            print("PISTAS: Puede ser uno de estos jugadores")
            for indice, LakersPlayer in enumerate(LakersList, 1):
                print(indice, LakersPlayer)

        if machineChoice in ClippersList:
            print("PISTAS: Puede ser uno de estos jugadores")
            for indice, ClippersPlayer in enumerate(ClippersList, 1):
                print(indice, ClippersPlayer)

        if machineChoice in HoustonList:
            print("PISTAS: Puede ser uno de estos jugadores")
            for indice, HoustonPlayer in enumerate(HoustonList, 1):
                print(indice, HoustonPlayer)

        playerChoice = input("\nAdivina el Jugador de la NBA: ").upper()

        # Calculo final del tiempo para evaluar cuanto tardó el usuario en adivinar el número
        # round() redondea el tiempo y el cero es para dar número flotante (3.0).
        tiempoFinal = time.time()
        tiempoResult = round(tiempoFinal - tiempoInicial, 0)

        # Condición comparando el jugador dado por el usuario y el jugador dado por la máquina
        if playerChoice == machineChoice:
            print("\nFelicidades: Adivinaste el jugador (^_^)")
            
            # # Condición que determina el tiempo tomado por el usuario para adivinar el jugador.
            if tiempoResult <= 8:
                print(f"ERES UN GENI@: Tu tiempo fue de: {tiempoResult} segundos (^_^)")
            
            else:
                print(f"DEBES MEJORAR: Tu tiempo fue de: {tiempoResult} segundos (~_~)")

            winnerCounter = winnerCounter + 1

        else:
            print(f"\nPerdiste: El jugador era {machineChoice} (~_~)")

            lostCounter = lostCounter + 1

        salir = input('''\nDeseas continuar jugando
                    1 - Si
                    2 - No ''').lower()

        if salir == "no":

            # Mostrar los número de aciertos y desaciertos del usuario.
            print(f"\nNumeros de aciertos: {winnerCounter} ")
            print(f"Numeros de desaciertos: {lostCounter}\n")
            input("Presione Enter para continuar....")
            break





                    