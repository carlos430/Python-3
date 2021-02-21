import os
import sqlite3
from setupCarpet import menu_main

def crearBD():
    # Crear la tabla Usuario.
    name = "Users.db"
    if name not in os.listdir("."):

        conexion = sqlite3.connect("Users.db")
        cursorData = conexion.cursor()

        cursorData.execute('''CREATE TABLE IF NOT EXISTS Usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user VARCHAR(20) UNIQUE NOT NULL,
                password VARCHAR(20) NOT NULL);''')

        conexion.close()
        print("Base de Datos Creada")

def insertUsers(user, password):
    # Insertar datos de usuarios en la tabla de usuario.
    conexion = sqlite3.connect("Users.db")
    cursorData = conexion.cursor()

    try:
        cursorData.execute("INSERT INTO Usuarios VALUES(NULL, ?, ?)",(user, password))

    except sqlite3.IntegrityError:
        print(f"El {user} ya existe")

    else:
        print(f"El usuario {user} fue creado satifactoriamente")

    conexion.commit()
    conexion.close()

def searchUsers(user, password):
    # Buscar usuario en la base de datos para realizar el logueo.
    conexion = sqlite3.connect("Users.db")
    cursorData = conexion.cursor()

    cursorData.execute("SELECT * FROM Usuarios WHERE user = ? AND password = ?",(user, password))
    rows = cursorData.fetchall()
    for item in rows:
        if item[1] == user and item[2] == password:
            menu_main.menu(item[1])
