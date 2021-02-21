#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 03:05:20 2021
@author: Carlos Javier Fenelon Laureano
"""
import re
import sqlite3
from prettytable import PrettyTable

class BaseDataClass:
    def __init__(self, TodoData):
        self.conexion = sqlite3.connect(TodoData)
        self.cursor = self.conexion.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ToDoList(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarea VARCHAR(50) NOT NULL,
            fecha VARCHAR(50) NOT NULL,
            status VARCHAR(20) DEFAULT "NO REALIZADA(X)");''')

        self.conexion.commit()
                   
    def insertData_ToDoList(self, tarea, fecha, status):
        self.cursor.execute("INSERT INTO ToDoList VALUES(NULL, ?, ?, ?)",(tarea, fecha, status))
        self.conexion.commit()

    def mostrarTareas(self):
        """ Instalar el modulo PrettyTable y utilizarlo 
            para crear tablas mas elegantes (from prettytable import PrettyTable). """

        self.cursor.execute("SELECT * FROM ToDoList")
        rows = self.cursor.fetchall()
        mytable = PrettyTable(["ID", "TAREAS", "FECHA CREACION", "STATUS"])
        for item in rows:
           mytable.add_row([item[0], item[1], item[2], item[3]])
        print(mytable)

    def searchTask_Db(self, tarea):
        """ Utilizar expresiones regulares para hacer busquedas avanzadas en la lista de tareas."""

        self.cursor.execute("SELECT * FROM TodoList")
        rows = self.cursor.fetchall()
        mytable = PrettyTable(["ID", "TAREAS", "FECHA CREACION", "STATUS"])
        for item in rows:
            if re.findall(tarea, item[1]):
                mytable.add_row([item[0], item[1], item[2], item[3]])
        print(mytable)
              
    def update_task(self, id, tarea):
        self.cursor.execute("UPDATE ToDoList SET tarea = ? WHERE id = ?",(tarea, id))
        self.conexion.commit()

    def makeTask_db(self, id, status):
        self.cursor.execute("UPDATE ToDoList SET status = ? WHERE id = ?",(status, id))
        self.conexion.commit()

    def erase_task(self, id):
            self.cursor.execute("DELETE FROM ToDoList WHERE id = ?",(id,))
            self.conexion.commit()

    def __del__(self):
        self.conexion.close()