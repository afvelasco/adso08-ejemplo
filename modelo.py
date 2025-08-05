class Productos:
    def __init__(self):
        self.listado = []
    
    def agregar(self, un_producto):
        self.listado.append(un_producto)
    
    def buscar(self, cod): # retorna la posición donde encuentra el código o -1 si no lo encuentra
        n = len(self.listado)
        pos = -1 # se supone que no se encuentra
        for i in range(0,n,1):
            if self.listado[i]["codigo"]==cod:
                pos = i # lo encontramos y corregimos
                break
        return pos
    
    def busca_prod(self,cod):
        pos = self.buscar(cod)
        if pos>=0:
            print(self.listado[pos])
        else:
            print("No encontrado")

    def modificar(self, nuevo_producto):
        pos = self.buscar(nuevo_producto["codigo"])
        if pos>=0:
            self.listado[pos] = nuevo_producto
        else:
            print("Producto no encontrado")

    def borrar(self, cod):
        pos = self.buscar(cod)
        if pos>=0:
            self.listado.remove(self.listado[pos])
        else:
            print("Producto no encontrado")

    def listar(self):
        n = len(self.listado)
        for i in range(0,n,1):
            print(self.listado[i])
