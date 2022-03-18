import os
import sqlite3
from producto import productos


def ingresar():
    correo = input("correo: ")
    contrasena = input("contraseña: ")
    print("---------------------------------------------------------------------------")
    con_bd = sqlite3.connect('db.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT contrasena FROM usuarios WHERE correo ='"+correo+"'and contrasena='"+contrasena+"'"
    cursor_db.execute(sql)
    if cursor_db.fetchall():
        print("ingreso exitoso")
        print("---------------------------------------------------------------------------")
        return productos()
    else:
        print("correo o contraseña invalidos \n INTENTE DE NUEVO... ")
        return ingresar()


