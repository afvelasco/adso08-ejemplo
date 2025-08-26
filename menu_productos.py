import json
from modelo_productos import Productos

def productos():
    try:
        with open("productos.json", "r", encoding="utf-8") as archivo_p:
            listado_p = json.load(archivo_p)
    except FileNotFoundError:
        listado_p = []
    mis_productos = Productos(listado_p) 
    while True:
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Modificar producto")
        print("4. Borrar producto")
        print("5. Listar")
        print("\n0. Regresar")
        opcion = input("\nQue opción desea? ")
        if opcion=="1":
            codigo=input("Digite código: ")
            nombre=input("Digite nombre: ")
            precio=float(input("Digite precio: "))
            stock =int(input("Digite stock: "))
            un_producto={"codigo":codigo,"nombre":nombre,
                        "precio":precio,"stock":stock}
            resul = mis_productos.agregar(un_producto)
            if resul==0:
                print("Producto agregado exitosamente!")
            else:
                print("Código de producto ya existe!")
        elif opcion=="2":
            codigo=input("Digite código a buscar: ")
            resul = mis_productos.buscar(codigo)
            if resul==-1:
                print("Código de producto no encontrado!")
            else:
                print(listado_p[resul])
        elif opcion=="3":
            codigo=input("Digite código a modificar: ")
            resul = mis_productos.busca_prod(codigo)
            if resul==-1:
                print("Código de producto no encontrado!")
            else:
                nombre=input("Digite nuevo nombre: ")
                precio=float(input("Digite nuevo precio: "))
                stock =int(input("Digite nuevo stock: "))
                nuevo_producto={"codigo":codigo,"nombre":nombre,
                                "precio":precio,"stock":stock}
                mis_productos.modificar(nuevo_producto)
        elif opcion=="4":
            codigo=input("Digite código a borrar: ")
            resul = mis_productos.borrar(codigo)
            if resul==0:
                print("Producto borrado exitosamente!")
            else:
                print("Código de producto no encontrado!")
        elif opcion=="5":
            mis_productos.listar()
        elif opcion=="0":
            break
    with open("productos.json", "w", encoding="utf-8") as archivo_p:
        json.dump(listado_p, archivo_p, indent=4, ensure_ascii=False)
