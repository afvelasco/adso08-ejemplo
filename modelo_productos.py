class Productos:
    def __init__(self, listado):
        self.listado = listado
    
    def agregar(self, un_producto):
        pos = self.buscar(un_producto["codigo"])
        if pos==-1:
            self.listado.append(un_producto)
            return 0
        else:
            return 1
    
    def buscar(self, cod): # retorna la posición donde encuentra el código o -1 si no lo encuentra
        n = len(self.listado)
        pos = -1 # se supone que no se encuentra
        for i in range(0,n,1):
            if self.listado[i]["codigo"]==cod:
                pos = i # lo encontramos y corregimos
                break
        return pos
    
    def modificar(self, nuevo_producto):
        pos = self.buscar(nuevo_producto["codigo"])
        self.listado[pos] = nuevo_producto

    def borrar(self, cod):
        pos = self.buscar(cod)
        if pos>=0:
            self.listado.remove(self.listado[pos])
            return 0
        else:
            return 1

    def listar(self):
        n = len(self.listado)
        for i in range(0,n,1):
            print(self.listado[i])
