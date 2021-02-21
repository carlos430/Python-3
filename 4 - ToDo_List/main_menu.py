#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Jan 17 03:05:20 2021
@author: Carlos Javier Fenelon Laureano
"""

import os
from todoList import ToDo

task = ToDo()

def menu():
    while True:
        print("1 - VER TAREAS")
        print("2 - AGREGAR TAREAS")
        print("3 - REALIZAR TAREAS")
        print("4 - MODIFICAR TAREAS")
        print("5 - ELIMINAR TAREAS")
        print("6 - BUSCAR TAREAS")
        print("7 - EXIT")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                os.system("cls")
                task.showTask()

            elif opcion == 2:
                os.system("cls")
                tareas = input("AGREGAR TAREAS: ").upper()
                task.addTask(tareas)

            elif opcion == 3:
                os.system("cls")
                print("REALIZAR TAREA")
                id = int(input("Id de la tarea a realizar: "))
                task.makeTask(id)
                
            elif opcion == 4:
                os.system("cls")
                print("Modificar Tareas")
                id = int(input("Id de la tarea: "))
                tareas = input("Modificar Tarea: ").upper()
                task.modifyTask(id, tareas)          

            elif opcion == 5:
                os.system("cls")
                print("Eliminar Tareas")
                id = int(input("Id de la tarea a eliminar: "))
                task.elimate_task(id)

            elif opcion == 6:
                os.system("cls")
                tarea = input("Buscar Tareas: ").upper()
                task.searchTask(tarea)

            elif opcion == 7:
                print("Saliendo del Programa")
                break

        except ValueError:
            print("ERROR! Digite Un Numero Entero")

        else:
            print("Opcion Incorrecta\n")
            
if __name__ == "__main__":
    menu()