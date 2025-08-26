"""
Se trata de escribir un programa de computador que permita almacenar
una lista de productos (codigo, nombre, precio, stock). El programa 
debe ofrecer opciones para agregar un nuevo producto, buscar la infor-
mación de un producto a partir de su código, modificar un producto,
borrar un producto, listar todos los productos. El programa debe manejar
persistencia para los datos almacenados, utilizando MySQL o utilizando 
archivos planos con JSON

NOTA: Utilizar POO
"""
from modelo_clientes import Clientes
import json

def clientes():
    try:
        with open("clientes.json", "r", encoding="utf-8") as archivo_c:
            listado_c = json.load(archivo_c)
    except FileNotFoundError:
        listado_c = []
    mis_clientes = Clientes(listado_c) 
    while True:
        print("1. Agregar cliente")
        print("2. Buscar cliente")
        print("3. Modificar cliente")
        print("4. Borrar cliente")
        print("5. Listar")
        print("\n0. Regresar")
        opcion = input("\nQue opción desea? ")
        if opcion=="1":
            id=input("Digite id: ")
            nombre=input("Digite nombre: ")
            saldo=float(input("Digite saldo: "))
            cupo =float(input("Digite cupo crédito: "))
            un_cliente={"id":id,"nombre":nombre,
                        "saldo":saldo,"cupo":cupo}
            resul = mis_clientes.agregar(un_cliente)
            if resul==0:
                print("Cliente agregado exitosamente!")
            else:
                print("Id de cliente ya existe!")
        elif opcion=="2":
            id=input("Digite id a buscar: ")
            resul = mis_clientes.buscar(id)
            if resul==-1:
                print("Id de cliente no encontrado!")
            else:
                print(listado_c[resul])
        elif opcion=="3":
            id=input("Digite id a modificar: ")
            resul = mis_clientes.busca_prod(id)
            if resul==-1:
                print("Id de cliente no encontrado!")
            else:
                nombre=input("Digite nuevo nombre: ")
                saldo=float(input("Digite nuevo saldo: "))
                cupo=float(input("Digite nuevo cupo crédito: "))
                nuevo_producto={"id":id,"nombre":nombre,
                                "saldo":saldo,"cupo":cupo}
                mis_clientes.modificar(nuevo_producto)
        elif opcion=="4":
            id=input("Digite id a borrar: ")
            resul = mis_clientes.borrar(id)
            if resul==0:
                print("Cliente borrado exitosamente!")
            else:
                print("Id de cliente no encontrado!")
        elif opcion=="5":
            mis_clientes.listar()
        elif opcion=="0":
            break
    with open("clientes.json", "w", encoding="utf-8") as archivo_c:
        json.dump(listado_c, archivo_c, indent=4, ensure_ascii=False)

