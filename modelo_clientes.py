"""
Se trata de escribir un programa con un CRUD para clientes
Cada producto debe tener los siguientes datos:
IdentificaciOn (string), Nombre (string), saldo (float), 
cupo_crédito (float)
"""
class Clientes: 
    def __init__(self, listado):
        self.listado = listado
    
    def agregar(self, un_cliente):
        pos = self.buscar(un_cliente["id"])
        if pos==-1:
            self.listado.append(un_cliente)
            return 0
        else:
            return 1
    
    def buscar(self, id): # retorna la posición donde encuentra el id o -1 si no lo encuentra
        n = len(self.listado)
        pos = -1 # se supone que no se encuentra
        for i in range(0,n,1):
            if self.listado[i]["id"]==id:
                pos = i # lo encontramos y corregimos
                break
        return pos
    
    def modificar(self, nuevo_cliente):
        pos = self.buscar(nuevo_cliente["id"])
        self.listado[pos] = nuevo_cliente

    def borrar(self, id):
        pos = self.buscar(id)
        if pos>=0:
            self.listado.remove(self.listado[pos])
            return 0
        else:
            return 1

    def listar(self):
        n = len(self.listado)
        for i in range(0,n,1):
            print(self.listado[i])
