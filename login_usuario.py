# openpyxl
from openpyxl import *
from openpyxl import Workbook

def loginUsuario():
    #Iniciamos el excel
    book = load_workbook('bd_login.xlsx')
    
    #Recuperamos la cantidad de columnas
    max_row=book.active.max_row
    
    #Datos de usuario
    userName = input("Ingresa nombre de usuario: ")
    password = input("Ingresa nombre de contraseña: ")
    
    #Activar la edicion
    sheet = book.active
    for i in range(max_row):
        #Iniciamos en la fila 2
        variableApoyo = i + 2
        userConfi = sheet[f"B{variableApoyo}"]
        passConfi = sheet[f"C{variableApoyo}"]
        # value nos da el valor de excel
        if userName == userConfi.value:
            if password == passConfi.value:
                print("El usuario se ha logueado con exito")
                return True
    else:
        print("Contraseña o usuario incorrectos")
loginUsuario()