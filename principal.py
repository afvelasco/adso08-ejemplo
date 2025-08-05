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
from modelo import Productos
mi_listado = Productos() 
while True:
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Modificar producto")
    print("4. Borrar producto")
    print("5. Listar")
    print("\n0. Salir")
    opcion = input("\nQue opción desea? ")
    if opcion=="1":
        codigo=input("Digite código: ")
        nombre=input("Digite nombre: ")
        precio=input("Digite precio: ")
        stock =input("Digite stock: ")
        un_producto={"codigo":codigo,"nombre":nombre,
                     "precio":precio,"stock":stock}
        mi_listado.agregar(un_producto)
    elif opcion=="2":
        codigo=input("Digite código a buscar: ")
        mi_listado.busca_prod(codigo)
    elif opcion=="3":
        codigo=input("Digite código a modificar: ")
        nombre=input("Digite nuevo nombre: ")
        precio=input("Digite nuevo precio: ")
        stock =input("Digite nuevo stock: ")
        nuevo_producto={"codigo":codigo,"nombre":nombre,
                        "precio":precio,"stock":stock}
        mi_listado.modificar(nuevo_producto)
    elif opcion=="4":
        codigo=input("Digite código a borrar: ")
        mi_listado.borrar(codigo)
    elif opcion=="5":
        mi_listado.listar()
    elif opcion=="0":
        break
