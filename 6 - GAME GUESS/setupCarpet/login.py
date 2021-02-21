""" Sistema de Registros y Entrada de Usuario """
from setupCarpet import menu_main
from setupCarpet import setup
from setupCarpet import baseData
from getpass import getpass

# Modulo de control de usuario.
def login_main():

    baseData.crearBD()

    while True:
        print("############## Control De Usuario ##############")
        print("#\t\t1 - Iniciar Sesion            #")
        print("#\t\t2 - Registrarse               #")
        print("#\t\t3 - Salir                     #")
        print("###############################################")
        opcion = setup.typeNumber("Seleccione una opcion: ")

        if opcion == 1:
            user = input("Usuario: ")
            password = getpass("Contraseña: ")
            baseData.searchUsers(user, password)
            
        elif opcion == 2:
            user = input("Usuario: ")
            password = input("Contraseña: ")
            baseData.insertUsers(user, password)

        elif opcion == 3:
            print("Saliste del juego (^_^)")
            break

        else:
            print("Seleccione una opcion correcta")