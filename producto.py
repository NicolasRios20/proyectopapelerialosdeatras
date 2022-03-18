import os
import sqlite3


def productos():
    con_bd = sqlite3.connect('db.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT * FROM productos"
    cursor_db.execute(sql)
    productos = cursor_db.fetchall()
    for fila in productos:
        print(*fila)
    print("---------------------------------------------------------------------------")
    compra = input("ingrese 1 para adquierir productos: ")
    print("---------------------------------------------------------------------------")
    if compra == "1":
        return comprar()
    else:
        print("gracias por visitarnos")


total = 0  
def comprar():
    global total
    adquirir = input("ingrese el nombre del producto: ")
    print("---------------------------------------------------------------------------")
    con_bd = sqlite3.connect('db.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT precio FROM productos WHERE nombre_producto='"+adquirir+"'"
    cursor_db.execute(sql)
    consulta=cursor_db.fetchone()
    print(f"{adquirir} tiene un precio de: ",*consulta)
    print("---------------------------------------------------------------------------")
    cantidad = int(input("cuantas unidades desea: "))
    cantidad = cantidad * int(consulta[0])
    print(f"la cantidad de {adquirir} tiene un precio de: ",cantidad)
    print("---------------------------------------------------------------------------")
    total = total + cantidad
    compra = int(input("¿Desea comprar otro producto? (si) ingrese 1 (no) ingrese 0: "))
    if compra == 1:
        return productos()
    else:
        print(f"el valor total a pagar es {total}")
        

