from baseData import BaseDataClass

datosUsers = BaseDataClass("TodoData.db")

def login_main():

    while True:
        print("############## Control De Usuario ##############")
        print("#\t\t1 - Iniciar Sesion            #")
        print("#\t\t2 - Registrarse               #")
        print("#\t\t3 - Salir                     #")
        print("###############################################")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            user = input("Usuario: ")
            password = input("Contraseña: ")
            datosUsers.login_user_bd(user, password)
            
        elif opcion == 2:
            user = input("Usuario: ")
            password = input("Contraseña: ")
            datosUsers.register_user_bd(user, password)

        elif opcion == 3:
            print("Saliste del Programa (^_^)")
            break

        else:
            print("Seleccione una opcion correcta")

login_main()