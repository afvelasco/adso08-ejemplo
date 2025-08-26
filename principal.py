from menu_clientes import clientes
from menu_productos import productos

while True:
    print("")
    print("")
    print("")
    print("")
    print("#############################################")
    print("1. Gestión de productos")
    print("2. Gestión de clientes\n")
    print("0. Salir")
    opcion = input("Digita la opción deseada: ")
    if opcion=="1":
        productos()
    elif opcion=="2":
        clientes()
    elif opcion=="0":
        break

