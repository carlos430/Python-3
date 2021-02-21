# Adivina el numero o el personaje

""" Menu Interactivo del juego"""

from setupCarpet import setup
from setupCarpet import baseData
from Guess_Number import EasyLevel
from Guess_Number import HardLevel
from Guess_Person import NbaPerson
from PaperScissorsRock import PiedraPapelTijera

# Menu principal del juego.

def menu(user):

    while True:
        setup.clear()
        print("############## EL ADIVINADOR ##############")
        print("#                                         #")
        print(f"\tUSUARIO CONECTADO: {user}               ")
        print("#                                         #")
        print("###########################################")
        print("#\t1 - Adivina el Numero             #")
        print("#\t2 - Adivina el personaje          #")
        print("#\t3 - Piedra, Paper, Tijera         #")
        print("#\t4 - Salir                         #")
        print("###########################################")

        opcion = setup.typeNumber("Digite un opcion: ")

        if opcion == 1:

            while True:
                # Menu para entrar al modulo de Adivina el numero.
                setup.clear()

                print("############## Adivina el Numero ##############")
                print("# \t\t  Niveles                     #")
                print("#\t\t1 - Facil                     #")
                print("#\t\t2 - Dificil                   #")
                print("#\t\t3 - Salir                     #")
                print("###############################################")
                                
                opcion2 = setup.typeNumber("Digite un opcion: ")

                if opcion2 == 1:
                    EasyLevel.easy()
                
                elif opcion2 == 2:
                    HardLevel.hard()
                        
                elif opcion2 == 3:
                    break

                else:
                    print("seleccione una opcion valida")

        elif opcion == 2:

            while True:
                setup.clear()
                print("############## Adivina el Personaje ##############")
                print("# \t\t  Profesiones                    #")
                print("#\t\t 1 - NBA                         #")
                print("#\t\t 2 - Salir                       #")
                print("##################################################")
                opcion_person = setup.typeNumber("Digite un opcion: ")

                if opcion_person == 1:
                    NbaPerson.nba_player()

                elif opcion_person == 2:
                    break

                else:
                    print("Seleccione una opcion correcta")

        elif opcion == 3:
            PiedraPapelTijera.piedra_papel_tijera()
                    
        elif opcion == 4:
            print("Saliste del juego (^_^)")
            break

        else:
            print("Selecciones una opcion valida")
       