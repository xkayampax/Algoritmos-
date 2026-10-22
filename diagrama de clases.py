class Fiesta:

    def __init__(self, clave, presupuesto):
        self.clave = clave
        self.presupuesto = presupuesto

    def ver_ingreso(self):
        pass

    def agregar_invitados(self):
        pass

    def realizar_presupuesto(self):
            pass

class Invitados:
    
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.clave = clave

    def recibir_invitacion(self):
        pass

    def ingresar_fiesta(self):
        pass

    def consumir_alimento(self):
        pass


class Alimento:

    def __init__(self, cantidad, nombre, precio):
        self.cantidad = cantidad
        self.nombre = nombre
        self.precio = precio

    def preparar_comida(self):
        pass

    def consumirlos(self):
        pass

    