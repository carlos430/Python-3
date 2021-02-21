#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Jan 17 03:05:20 2021
@author: Carlos Javier Fenelon Laureano
"""

import datetime
from baseData import BaseDataClass

datos = BaseDataClass("TodoData.db")

 
class ToDo:
# Clase ToDo inicializando las variables tarea y tiempo.

    def __init__(self, tarea=""):
        self.tarea = tarea
        self.time = datetime.datetime.now()

    # Metodo de agregar tareas con su tiempo y un status por default en NO REALIZADA.
    def addTask(self, tareas, status="NO REALIZADA(X)"):
        currentDate = self.time.strftime("%I:%M:%p %d/%h/%Y")
        datos.insertData_ToDoList(tareas, currentDate, status)

    # Metodo de marcar las tareas ya realizadas.
    def makeTask(self, id, status="REALIZADA(✓)"):
        datos.makeTask_db(id, status)

    # Metodo de modificar las tareas ya agregadas en la base de datos.
    def modifyTask(self, id, tareas):
        datos.update_task(id, tareas)

    # Metodo para mostrar todas las tareas guardadas en la base datos.
    def showTask(self):
        datos.mostrarTareas()
    
    # Metodo para eliminar las tareas por su Id.  
    def elimate_task(self, id):
        datos.erase_task(id)

    def searchTask(self, tarea):
        datos.searchTask_Db(tarea)

    


