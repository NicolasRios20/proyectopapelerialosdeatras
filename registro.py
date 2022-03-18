import os
import sqlite3
from confirmacion_correo import confirmacion_correo
from ingreso import ingresar


def inicio():
    inicio_sesion = input("1 para iniciar sesion, 0 para registrarse: ")
    if inicio_sesion == "1":
        return ingresar()
    if inicio_sesion == "0":
        return registro()


def registro():
    global correo
    global contrasena
    nombre = input("ingrese un nombre de usuario: ")
    correo = input("ingrese su correo electronico: ")
    contrasena = input("ingrese su contraseña: ")
    edad = int(input("edad: "))
    ciudad = input("ciudad: ")
    telefono = input("telefono: ")
    print("---------------------------------------------------------------------------")
    con_bd = sqlite3.connect('db.db')
    cursor_db = con_bd.cursor()
    sql = "INSERT INTO usuarios(nombre,correo,contrasena,edad,ciudad,telefono)VALUES(?,?,?,?,?,?)"
    try:
        cursor_db.execute(sql, (nombre,correo,contrasena,edad,ciudad,telefono))
        con_bd.commit()
        cursor_db.close()
        return confirmacion_correo(correo)
        
    except:
        print("el correo ya existe")